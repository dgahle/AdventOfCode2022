# Imports
from argparse import ArgumentParser
from os import mkdir
from pathlib import Path
from shutil import copy
from typing import Any

# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent
INPUT_DIR_PATH: Path = REPO_PATH / 'input'
PYTHON_SCRIPTS_DIR_PATH: Path = REPO_PATH / 'python' / 'scripts'
PYTHON_TEMPLATE_PATH: Path = REPO_PATH / 'python' / 'template.py'


# Argparse
parser: ArgumentParser = ArgumentParser()
parser.add_argument("--day", type=int, default=None, help="Day (int) of the Advent of Code.")
args: Any = parser.parse_args()


# Functions
def main() -> None:
    # Variable declaration
    day: int = args.day
    # Make new folders
    dir_paths: list[Path] = [
        INPUT_DIR_PATH,
        PYTHON_SCRIPTS_DIR_PATH
    ]
    for dir_path in dir_paths:
        new_dir_path: Path = dir_path / f'day_{day}'
        new_dir: str = str(new_dir_path)
        mkdir(new_dir)
    # Make new scripts (by copying the template.py
    script: str
    scripts: list[str] = [
        'functions',
        'main',
        'tests'
    ]
    scripts_dir: Path = PYTHON_SCRIPTS_DIR_PATH / f'day_{day}'
    template_path: str = str(PYTHON_TEMPLATE_PATH)
    for script in scripts:
        script_path: Path = scripts_dir / f'{script}.py'
        script_path: str = str(script_path)
        copy(template_path, script_path)
    pass


if __name__ == "__main__":
    main()
