# Imports
from pathlib import Path
from python.scripts.day_6.functions import get_index_of_first_packet

# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_DIR_PATH: Path = REPO_PATH / 'input' / 'day_6'
INPUT_DATA_PATH: Path = INPUT_DIR_PATH / 'input.txt'
PYTHON_SCRIPTS_DIR_PATH: Path = REPO_PATH / 'python' / 'scripts'


# Functions
def main() -> None:
    """
    To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker
    in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of
    four characters that are all different.

    Part 1: How many characters need to be processed before the first start-of-packet marker is detected?

    :return None:
    """
    # Read data
    with open(INPUT_DATA_PATH, 'r') as f:
        data: str = f.read()
    # Find index
    part: int
    scanning_len: int
    scanning_lengths: list[int] = [4, 14]
    for part, scanning_len in enumerate(scanning_lengths):
        part += 1
        index: int = get_index_of_first_packet(data, unique_len=scanning_len)
        task_msg: str = 'How many characters need to be processed before the first start-of-packet marker is detected.'
        print(f'Part {part}: {task_msg}')
        print(f"{' '*4} = {index} characters (with unique length of {scanning_len})")


if __name__ == "__main__":
    main()
