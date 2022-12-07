# Imports
from pathlib import Path
from python.scripts.day_5.functions import SolvePuzzle


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_5' / 'input.txt'


# Functions
def main() -> None:
    # Play the game
    num_part: int
    reverse: bool
    reverse_cmds: list[bool] = [True, False]
    for num_part, reverse in enumerate(reverse_cmds):
        num_part += 1
        # Load puzzle
        puzzle: SolvePuzzle = SolvePuzzle(INPUT_PATH)
        puzzle.solve(callback=False, reverse_order=reverse)
        answer: str = puzzle.solution
        # Read and print the answer
        print(f'Part {num_part}) After the rearrangement procedure completes, what crate ends up on top of each stack?')
        answer_msg: str = f"{' '*4} - {answer}"
        print(answer_msg)
    pass


if __name__ == "__main__":
    main()
