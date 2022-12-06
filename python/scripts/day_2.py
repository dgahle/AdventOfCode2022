# Imports
from numpy import array, ndarray
from pandas import concat, DataFrame, merge, read_csv, read_excel
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
    Draw = 3 points

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
    assert score == expected_score, assert_msg


def part_1() -> None:
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
    # Load
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(INPUT_PATH, sep=' ', names=columns)
    # Calculate the score
    score: int = rock_paper_scissors_by_key(df)
    msg: str = f"Part 1) Total score for the antagonist is {score} points!"
    print(msg, end='\n\n')


def get_part_2_choice_points(df: DataFrame) -> int:
    """
    Order:
        - Keys -> Choice
        - Choice -> Outcome
        - Outcome -> Antagonist Choice
        - Antagonist Choice -> Choice Points
    :param df:
    :return:
    """
    # Step 1
    df_key_outcome: DataFrame = df_rules['key_outcome'].copy().rename(columns=dict(Key='Antagonist'))
    columns: list[str] = ['Opponent', 'Outcome']
    df = df.merge(df_key_outcome)  # [columns]
    df = df.merge(df_rules['outcome_points'])
    # Step 2
    df_mapping: DataFrame = df_match_points_mapping.copy()
    i_col: int
    col: str
    columns: list[str] = ['Opponent', 'Antagonist']
    frames: list[DataFrame] = []
    for i_col, col in enumerate(columns):
        _df: DataFrame = df_mapping['Match'].apply(lambda x: x[i_col]).to_frame(name=col)
        frames.append(_df)
    df_mapping = concat([*frames, df_mapping], axis=1)
    df_mapping = df_mapping.merge(df_rules['outcome_points'])
    col: str = 'Opponent-Outcome'
    frames = [
        df_mapping,
        df_mapping[['Opponent', 'Outcome']].sum(1).to_frame(col)
    ]
    df_mapping = concat(frames, axis=1)
    # Step 3
    df = df[['Opponent', 'Outcome']].sum(1).to_frame(col)
    df = df.merge(df_mapping[[col, 'Antagonist']])
    df = df.rename(columns=dict(Antagonist='Key'))
    df = df.merge(df_rules['key_choice'][['Key', 'Choice']])
    df = df.merge(df_rules['choice_points'])
    # Step 4
    choice_points: int = df['Points'].sum()
    return choice_points


def get_part_2_match_score(df: DataFrame) -> int:
    """

    :param df:
    :return:
    """
    new_columns: str = 'Antagonist'
    df_antagonist_key_points: DataFrame = merge(df_rules['key_outcome'], df_rules['outcome_points'], on='Outcome',
                                                how='inner')
    df_antagonist_key_points = df_antagonist_key_points.rename(columns=dict(Key=new_columns))
    df_match_points: DataFrame = df[[new_columns]].merge(df_antagonist_key_points, on=new_columns, how='inner')
    match_points: int = df_match_points['Points'].sum()
    return match_points


def test_part_2() -> None:
    """

    :return:
    """
    # Load data
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(TEST_INPUT_PATH, sep=' ', names=columns)
    # Choice points
    choice_points: int = get_part_2_choice_points(df)
    # Match points
    match_points: int = get_part_2_match_score(df)
    # Calculate the score
    score: int = choice_points + match_points
    # Test
    expected_score: int = 12
    assert_msg: str = f"score ({score}) != expected_score ({expected_score})!"
    assert score == expected_score, assert_msg


def part_2() -> None:
    """
    The Elf finishes helping with the tent and sneaks back over to you:
        "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end
         the round in a draw, and Z means you need to win. Good luck!"

    The total score is still calculated in the same way, but now you need to figure out what shape to choose so the
    round ends as indicated.

    The example above now goes like this:

        In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you
        also choose Rock.
        This gives you a score of 1 + 3 = 4.
        In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of
        1 + 0 = 1.
        In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
        Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
    according to your strategy guide?

    :return:
    """
    # Load
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(INPUT_PATH, sep=' ', names=columns)
    # Choice points
    choice_points: int = get_part_2_choice_points(df)
    # Match points
    match_points: int = get_part_2_match_score(df)
    # Calculate the score
    score: int = choice_points + match_points
    msg: str = f"Part 2) Total score for the antagonist is {score} points!"
    print(msg)


def tests() -> None:
    """

    :return:
    """
    test_rock_paper_scissors_by_key()
    test_part_2()


def main() -> None:
    """

    :return None:
    """
    # Test functions
    tests()
    # Part 1
    part_1()
    # Part 2
    part_2()
    pass


if __name__ == "__main__":
    main()
