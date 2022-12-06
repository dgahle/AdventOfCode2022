# Imports
from numpy import array, ndarray
from pandas import concat, DataFrame, read_csv, read_excel
from pathlib import Path


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_2' / 'input.txt'
TEST_INPUT_PATH: Path = REPO_PATH / 'input' / 'day_2' / 'test_input.txt'
GAME_MAPPING_PATH: Path = REPO_PATH / 'input' / 'day_2' / 'rule_mappings.xlsx'
# Mappings
df_rules: dict[str, DataFrame] = read_excel(GAME_MAPPING_PATH, sheet_name=None)  # dict_keys(['key_choice', 'choice_points', 'outcome_points', 'rules'])


# Functions
def get_choice_mapping() -> None:
    """

    :return None:
    """
    if "df_key_points_mapping" not in globals():
        # Key-Points mapping
        columns: list[str] = ['Key', 'Points']
        df_key_points_mapping: DataFrame = df_rules['key_choice'].merge(df_rules['choice_points'], on='Choice')
        df_key_points_mapping = df_key_points_mapping[columns]
        globals()['df_key_points_mapping'] = df_key_points_mapping
    pass


def get_match_mapping() -> None:
    """
    Builds a mapping from the:
        - key formatted matches to the,
        - choice formatted matched to
        - the outcome,
        - the awarded points

    The resulting pandas.DataFrame (df_match_points_mapping) is made a global variable and will map the input to the
    match score.

    :return None:
    """
    if "df_match_points_mapping" not in globals():
        # Key -> Choice mapping
        pivot_kwargs: dict[str, str] = dict(
            columns='Player',
            index='Choice',
            values='Key'
        )
        df_key_choice: DataFrame = df_rules['key_choice'].pivot(**pivot_kwargs)
        df_key_choice.columns.name = None
        df_key_choice = df_key_choice.reset_index()
        # Choice -> outcome -> points mapping
        melt_kwargs: dict[str] = dict(
            id_vars=['Antagonist'],
            value_vars=None,
            var_name='Opponent',
            value_name='Outcome'
        )
        df_rules['rules'] = df_rules['rules'].melt(**melt_kwargs)
        df_rules['rules'] = df_rules['rules'].merge(df_rules['outcome_points'], on="Outcome")
        # Key -> Choice -> outcome -> points mapping
        col: str
        columns: list[str] = ['Antagonist', 'Opponent']
        # frames: list[DataFrame] = []
        _df: DataFrame = df_rules['rules'].copy()  # [_columns]
        for col in columns:
            _df = _df.rename(columns={col: 'Choice'})
            _df = _df.merge(df_key_choice[[col, 'Choice']], on='Choice')
            _df = _df[_df.columns[~_df.columns.isin(['Choice'])]]

        frames: list[DataFrame] = [
            _df[['Opponent', 'Antagonist']].sum(1).to_frame(name='Match'),
            _df[['Outcome', 'Points']]
        ]
        _df = concat(frames, axis=1)
        # Outcome mapping
        globals()['df_match_points_mapping']: DataFrame = _df[['Match', 'Points']]
    pass


def get_choice_points(df: DataFrame) -> int:
    """

    :param df:
    :return:
    """
    # Get mapping if it is not in globals()
    get_choice_mapping()
    # Get choice points
    df_choice: DataFrame = df[['Antagonist']].copy()
    df_choice = df_choice.rename(columns=dict(Antagonist='Key'))
    df_choice_points: DataFrame = df_choice.merge(df_key_points_mapping, on='Key', how='inner')
    choice_points: int = df_choice_points['Points'].sum()
    return choice_points


def get_match_points(df: DataFrame) -> int:
    """
    Calculates the points awarded to the antagonist for the outcome of the match.

    Win = 6 points
    Lose = 0 points
    Draw = 0 points

    :param (DataFrame) df: Long DataFrame of each round of the game in _key_ format
    :return (int) match_points: Points awarded to the Antagonist for winning, losing, or drawing
    """
    # Get mapping if it is not in globals()
    get_match_mapping()
    # Get match points
    name: str = 'Match'
    df_match: DataFrame = df.copy().sum(1).to_frame(name=name)
    df_match_points: DataFrame = df_match.merge(df_match_points_mapping, on=name)
    match_points: int = df_match_points['Points'].sum()
    return match_points


def rock_paper_scissors_by_key(df: DataFrame) -> int:
    """
    Takes rounds of Rock, Paper, Scissors as a long pandas.DataFrame in the _key_ format and calculates the points for
    the antagonist for their choices and wins (or losses/draws).

    :param (DataFrame) df: Long DataFrame of each round of the game in _key_format
    :return (int) total_points: Sum of points awarded to the antagonist for their choices and wins
    """
    # Choice points
    choice_points: int = get_choice_points(df)
    # Match points
    match_points: int = get_match_points(df)
    # Total points
    total_points: int = choice_points + match_points
    return total_points


def test_rock_paper_scissors_by_key() -> None:
    """
    `rock_paper_scissors_by_key` function can be tested against the provided strategy guide and test data.

    This strategy guide predicts and recommends the following:

        In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
            This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
        In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
            This ends in a loss for you with a score of 1 (1 + 0).
        The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
            In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    :return None:
    """
    # Load data
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(TEST_INPUT_PATH, sep=' ', names=columns)
    # Calculate the score
    score: int = rock_paper_scissors_by_key(df)
    # Test
    expected_score: int = 15
    assert_msg: str = f"score ({score}) != expected_score ({expected_score})!"
    assert score==expected_score, assert_msg


def main() -> None:
    """
    Task: What would your total score be if everything goes exactly according to your strategy guide?

    This strategy guide predicts and recommends the following:

        In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
            This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
        In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
            This ends in a loss for you with a score of 1 (1 + 0).
        The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
            In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    :return None:
    """
    # Test
    test_rock_paper_scissors_by_key()
    # Load
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(INPUT_PATH, sep=' ', names=columns)
    # Calculate the score
    score: int = rock_paper_scissors_by_key(df)
    msg: str = f"Total score for the antagonist is {score} points!"
    print(msg)
    pass


if __name__ == "__main__":
    main()
