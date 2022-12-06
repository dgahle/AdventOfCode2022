# Imports


# Variables


# Functions
def priority_letter_to_number(letter: str) -> int:
    """
    The conversion from letter to number (int) is by:
        - Lowercase item types a through z have priorities 1 through 26.
        - Uppercase item types A through Z have priorities 27 through 52.

    :param (str) letter:
    :return (int) number:
    """
    number: int
    # Capital
    if letter == letter.upper():
        number = ord(letter) - 38
    # Lower
    elif letter == letter.lower():
        number = ord(letter) - 96
    else:
        raise TypeError()

    return number


def get_priorities(data: list[str]) -> list[int]:
    """
    Each string entry in the data (list) has two parts that share a single letter that defines it's priority. The
    conversion from letter to number (int) is by:
        - Lowercase item types a through z have priorities 1 through 26.
        - Uppercase item types A through Z have priorities 27 through 52.

    :param (list[str]) data:
    :return (list[int]) priorities:
    """
    priorities: list[int] = []
    for d in data:
        i: int = len(d) // 2
        lhd: set = set(d[:i])
        rhd: set = set(d[i:])
        priority_letter: str = list(lhd.intersection(rhd))[0]
        priority_number: int = priority_letter_to_number(priority_letter)
        priorities.append(priority_number)

    return priorities


def get_group_priorities(data: list[str]) -> list[int]:
    """


    :param (list[str]) data:
    :return (list[int]) priorities:
    """
    priorities: list[int] = []
    group_size: int = 3
    number_of_groups: int = len(data) // group_size
    i_group: int
    for i_group in range(number_of_groups):
        lhs_index: int = i_group * group_size
        rhs_index: int = lhs_index + group_size
        group_index: slice = slice(lhs_index, rhs_index)
        group_data: list[str] = data[group_index]
        d: str
        group_data: list[set] = [set(d) for d in group_data]
        priority_letter: set = group_data[0].intersection(*group_data[1:])
        priority_letter: str = list(priority_letter)[0]
        priority_number: int = priority_letter_to_number(priority_letter)
        priorities.append(priority_number)

    return priorities

def main() -> None:
    pass


if __name__ == "__main__":
    main()
