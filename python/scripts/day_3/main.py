# Imports
from pathlib import Path
from python.scripts.day_3.functions import get_group_priorities, get_priorities


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_3' / 'input.txt'


# Functions
def part_1() -> None:
    """
    To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

    Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

    :return:
    """
    # Load data
    separator: str = '\n'
    with open(INPUT_PATH, 'r') as f:
        data: list[str] = f.read().split(separator)
    # Calculate priorities
    priorities: list = get_priorities(data)
    priorities_sum: int = sum(priorities)
    # Print message
    msg: str = f"Part 1) The sum of the priorities of those item types is {priorities_sum}"
    print(msg, end='\n\n')
    pass


def part_2() -> None:
    """

    :return None:
    """
    # Load data
    separator: str = '\n'
    with open(INPUT_PATH, 'r') as f:
        data: list[str] = f.read().split(separator)
    # Calculate priorities
    priorities: list = get_group_priorities(data)
    priorities_sum: int = sum(priorities)
    # Print message
    msg: str = f"Part 2) The sum of the priorities of those item types is {priorities_sum}"
    print(msg)
    pass


def main() -> None:
    part_1()
    part_2()
    pass


if __name__ == "__main__":
    main()
