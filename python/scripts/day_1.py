# Imports
from numpy import array, ndarray, sort
from pathlib import Path


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_1' / 'day_1_input.txt'


# Functions
def sum_str_list_of_ints(data: str, seperator: str) -> int:
    """
    Calculates the sum of numbers listed in a string.

    :param data:
    :param seperator:
    :return:
    """
    # To list
    data: list = data.split(seperator)
    # str -> int
    num: str
    data: ndarray = array([int(num) for num in data if len(num) > 0], dtype=int)
    # sum
    total: int = data.sum()
    return total


def main() -> None:
    """
    Tasks:
        Part 1 - Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
        Part 2 - Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

    Source: https://adventofcode.com/2022/day/1

    :return None:
    """
    # Load the data as a string
    with open(INPUT_PATH) as f:
        data: str = f.read()
    # Split by '\n'
    seperator: str = '\n\n'
    data: list[str] = data.split(seperator)
    # Convert to list of floats
    # Convert to numpy array
    d: str
    seperator: str = '\n'
    data: ndarray = array([sum_str_list_of_ints(d, seperator=seperator) for d in data])
    # Index of the elf with the most calories (plus one to start counting from 1)
    elf_index: int = data.argmax()
    elf_calories_max: int = data.max()
    part_1_answer: str = f'Part 1: Elf index {elf_index} has the most calories at {elf_calories_max} a.u.'
    print(part_1_answer, end='\n\n')
    # Sum of the three highest
    calories_of_the_top_three: int = sort(data)[-3:].sum()
    part_2_answer: str = f'Part 2: The top three elves have {calories_of_the_top_three} a.u calories.'
    print(part_2_answer)
    pass


if __name__ == "__main__":
    main()
