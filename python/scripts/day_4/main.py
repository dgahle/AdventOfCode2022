# Imports
from pathlib import Path
from python.scripts.day_4.functions import inclusion_check


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_4' / 'input.txt'


# Functions
def part_1() -> None:
    """
    Task: In how many assignment pairs does one range fully contain the other?

    Explaination: Some of the pairs have noticed that one of their assignments fully contains the other. For example,
    2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other,
    one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem
    like the most in need of reconsideration. In this example, there are 2 such pairs.

    :return None:
    """
    # Load data
    separator: str = '\n'
    with open(INPUT_PATH, 'r') as f:
        data: str = f.read()
    # Format into pairs
    data: list[str] = data.split(separator)
    d: list[str]
    separator: str = ','
    data: list[list[str]] = [d.split(separator) for d in data]
    # Inclusion check
    number_of_duplications: int = inclusion_check(data)
    # Print answer
    msg: str = f"Part 1) {number_of_duplications} assignment pairs does one range fully contain the other."
    print(msg, end='\n\n')
    # Inclusion check
    number_of_duplications: int = inclusion_check(data, total=False)
    # Print answer
    msg: str = f"Part 2) {number_of_duplications} assignment pairs do the ranges overlap."
    print(msg)

    pass


def part_2() -> None:
    pass


def main() -> None:
    part_1()
    part_2()
    pass


if __name__ == "__main__":
    main()
