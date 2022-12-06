# Imports
from pathlib import Path
from python.scripts.day_4.functions import inclusion_check


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
TEST_INPUT_PATH: Path = REPO_PATH / 'input' / 'day_4' / 'test_input.txt'


# Functions
def test_inclusion_check() -> None:
    """

    :return None:
    """
    # Load test data
    separator: str = '\n'
    with open(TEST_INPUT_PATH, 'r') as f:
        data: str = f.read()
    # Format into pairs
    data: list[str] = data.split(separator)
    d: list[str]
    separator: str = ','
    data: list[list[str]] = [d.split(separator) for d in data]
    # Check for inclusion
    num: int = inclusion_check(data)
    # Assert
    num_expectation: int = 2
    assert_msg: str = f"num {num} != {num_expectation}!"
    assert num == num_expectation, assert_msg


def test_inclusion_check_part2() -> None:
    """

    :return None:
    """
    # Load test data
    separator: str = '\n'
    with open(TEST_INPUT_PATH, 'r') as f:
        data: str = f.read()
    # Format into pairs
    data: list[str] = data.split(separator)
    d: list[str]
    separator: str = ','
    data: list[list[str]] = [d.split(separator) for d in data]
    # Check for inclusion
    num: int = inclusion_check(data, total=False)
    num_expectation: int = 4
    # Assert
    assert_msg: str = f"num {num} != {num_expectation}!"
    assert num == num_expectation, assert_msg


def main() -> None:
    test_inclusion_check()
    test_inclusion_check_part2()
    pass


if __name__ == "__main__":
    main()
