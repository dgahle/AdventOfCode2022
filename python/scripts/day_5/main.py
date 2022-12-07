# Imports
from pathlib import Path
from python.scripts.day_5.functions import SolvePuzzle


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_5' / 'input.txt'


# Functions
def main() -> None:
    # Load puzzle
    puzzle: SolvePuzzle = SolvePuzzle(INPUT_PATH)
    # Play the game
    puzzle.solve(callback=False)
    part_1_answer: str = puzzle.solution
    # Read and print the answer
    print('Part 1) After the rearrangement procedure completes, what crate ends up on top of each stack?')
    part_1_answer_msg: str = f"{' '*4} - {part_1_answer}"
    print(part_1_answer_msg)
    pass


if __name__ == "__main__":
    main()
