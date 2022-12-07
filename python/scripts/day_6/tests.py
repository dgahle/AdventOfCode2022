# Imports
from pandas import concat, DataFrame, read_csv
from pathlib import Path
from python.scripts.day_6.functions import get_index_of_first_packet


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_DIR_PATH: Path = REPO_PATH / 'input' / 'day_6'
TEST_DATA_PATH: Path = INPUT_DIR_PATH / 'test_data.csv'
TEST_DATA_PART_2_PATH: Path = INPUT_DIR_PATH / 'test_data_part_2.csv'
PYTHON_SCRIPTS_DIR_PATH: Path = REPO_PATH / 'python' / 'scripts'


# Functions
def test_get_index_of_first_packet() -> None:
    """

    :return:
    """
    # Load test data
    df: DataFrame = read_csv(TEST_DATA_PATH)
    # Run function
    name: str = 'trial'
    df_output: DataFrame = df['input'].apply(
        get_index_of_first_packet,
        args=[4]
    ).to_frame(name)
    # Group
    frames: list[DataFrame] = [df, df_output]
    df = concat(frames, axis=1)
    # Assert check
    assert df['output'].equals(df['trial'])


def test2_get_index_of_first_packet() -> None:
    """

    :return:
    """
    # Load test data
    df: DataFrame = read_csv(TEST_DATA_PART_2_PATH)
    # Run function
    name: str = 'trial'
    df_output: DataFrame = df['input'].apply(
        get_index_of_first_packet,
        args=[14]
    ).to_frame(name)
    # Group
    frames: list[DataFrame] = [df, df_output]
    df = concat(frames, axis=1)
    # Assert check
    assert df['output'].equals(df['trial'])


def main() -> None:
    test_get_index_of_first_packet()
    test2_get_index_of_first_packet()
    pass


if __name__ == "__main__":
    main()
