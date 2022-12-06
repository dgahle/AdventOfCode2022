# Imports
from pathlib import Path
from python.scripts.day_3.functions import get_priorities


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
TEST_INPUT_PATH: Path = REPO_PATH / 'input' / 'day_3' / 'test_input.txt'
TEST_ANSWER_PATH: Path = REPO_PATH / 'input' / 'day_3' / 'test_answer.txt'


# Functions
def test_part_1() -> None:
    # Load data
    separator: str = '\n'
    with open(TEST_INPUT_PATH, 'r') as f:
        data: list[str] = f.read().split(separator)
    # Calculate priorities
    priorities: list = get_priorities(data)
    # Load answer
    with open(TEST_ANSWER_PATH, 'r') as f:
        expectation: list[str] = f.read().split(separator)
    e: str
    expectation: list[int] = [int(e) for e in expectation]
    # Test
    assert_msg: str = f""
    assert all([a == b for a, b in zip(priorities, expectation)]), assert_msg


def main() -> None:
    test_part_1()
    pass


if __name__ == "__main__":
    main()
