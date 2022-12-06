# Imports
from numpy import arange, ndarray


# Functions
def _inclusion_check(data: list[str]) -> bool:
    """

    :param data:
    :return:
    """
    # From strings to ndarrays
    data0: ndarray = arange(*[int(d) + i for i, d in enumerate(data[0].split('-'))])
    data1: ndarray = arange(*[int(d) + i for i, d in enumerate(data[1].split('-'))])
    # Comparison
    check0: bool = all(d in data0 for d in data1)
    check1: bool = all(d in data1 for d in data0)
    check: bool = check0 or check1
    return check


def inclusion_check(data: list[[str]]) -> int:
    """

    :param data:
    :return:
    """
    check: list[bool] = [_inclusion_check(d) for d in data]
    num: int = sum(check)
    return num


def main() -> None:
    pass

if __name__ == "__main__":
    main()
