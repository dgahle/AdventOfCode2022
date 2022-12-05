# Imports
from numpy import array, ndarray
from pandas import DataFrame, read_csv, read_excel
from pathlib import Path


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_2' / 'input.txt'
GAME_MAPPING_PATH: Path = REPO_PATH / 'input' / 'day_2' / 'rule_mappings.xlsx'


# Functions
def main() -> None:
    """
    Task:
        This strategy guide predicts and recommends the following:

            In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
                This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
            In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
                This ends in a loss for you with a score of 1 (1 + 0).
            The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
                In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    What would your total score be if everything goes exactly according to your strategy guide?

    :return None:
    """
    # Load
    columns: list[str] = ['Opponent', 'Antagonist']
    df: DataFrame = read_csv(INPUT_PATH, sep=' ', names=columns)
    # Formatting
    df_rules: dict[str, DataFrame] = read_excel(GAME_MAPPING_PATH, sheet_name=None)
    # dict_keys(['key_choice', 'choice_points', 'outcome_points', 'rules'])
    # Key-Points mapping
    columns: list[str] = ['Key', 'Points']
    df_key_points_mapping: DataFrame = df_rules['key_choice'].merge(df_rules['choice_points'], on='Choice')
    df_key_points_mapping = df_key_points_mapping[columns]
    # Outcome mapping
    melt_kwargs: dict[str] = dict(
        id_vars=['Antagonist'],
        value_vars=None,
        var_name='Opponent',
        value_name='Outcome'
    )
    df_rules['rules'] = df_rules['rules'].melt(**melt_kwargs)
    df_rules['rules'] = df_rules['rules'].merge(df_rules['outcome_points'], on="Outcome")
    data: list = [
        df_rules['rules'][['Antagonist', 'Opponent']].sum(1).tolist(),
        df_rules['rules']['Points'].tolist()
    ]
    df_outcome_points: DataFrame = DataFrame(array(data).T.tolist(), columns=['Match', 'Points'])
    #
    #
    #
    # Choice points
    # print(
    #     df[['Antagonist']].copy().rename(
    #         columns=dict(Antagonist='Key')
    #     ).merge(
    #         df_key_points_mapping, on='Key'
    #     )
    # )
    # Outcome points
    print(
        # df[['Antagonist', 'Opponent']]
    )
    # print(
    #     df[['Antagonist']].copy().rename(
    #         columns=dict(Antagonist='Key')
    #     ).merge(
    #         df_key_points_mapping, on='Key'
    #     )
    # )
    # Total points
    pass


if __name__ == "__main__":
    main()
