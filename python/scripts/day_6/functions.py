# Imports
from pathlib import Path


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_DIR_PATH: Path = REPO_PATH / 'input'
PYTHON_SCRIPTS_DIR_PATH: Path = REPO_PATH / 'python' / 'scripts'


# Functions
def get_index_of_first_packet(data: str) -> int:
    """
    In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that
    are all different.

    :param (str) data:
    :return (int) index:
    """
    index: int
    unique_len: int = 4
    scan_len: int = len(data) - unique_len
    for index in range(scan_len):
        slice_stop: int = index + unique_len
        chunk_slice: slice = slice(index, slice_stop)
        chunk: str = data[chunk_slice]
        check: bool = len(chunk) == len(set(chunk))
        if check:
            return slice_stop


def main() -> None:
    pass


if __name__ == "__main__":
    main()
