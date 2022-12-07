# Imports
from numpy import ndarray
from pathlib import Path
from python.scripts.day_5.functions import preprocess_inputs, preprocess_puzzle, read_the_top, take_step


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_DIR_PATH: Path = REPO_PATH / 'input' / 'day_5'
TEST_INPUT_PATH: Path = INPUT_DIR_PATH / 'test_input.txt'
TEST_OUTPUT_PATH: Path = INPUT_DIR_PATH / 'test_output.txt'
TEST_OUTPUT_STEP_1_PATH: Path = INPUT_DIR_PATH / 'test_output_step_1.txt'
TEST_OUTPUT_STEP_4_PATH: Path = INPUT_DIR_PATH / 'test_output_step_4.txt'


# Functions
def test_read_the_top() -> None:
    # Load data
    # Input
    with open(TEST_OUTPUT_STEP_4_PATH, 'r') as f:
        data: str = f.read()
    # Expectation
    with open(TEST_OUTPUT_PATH, 'r') as f:
        expectation: str = f.read()
    # Run function
    data: ndarray = preprocess_puzzle(data)
    output: str = read_the_top(data)
    # Compare against expectation
    assert_msg: str = f"expectation ({expectation}) != output ({output})!"
    assert expectation == output, assert_msg


def test_take_step() -> None:
    # Load data
    with open(TEST_INPUT_PATH, 'r') as f:
        data_raw: str = f.read()
    # Preprocess inputs
    data: ndarray
    instructions: list[str]
    data, instructions = preprocess_inputs(data_raw)
    # Take step
    num_test: int
    result: ndarray
    step: int
    num_test: int = 1
    for step in range(num_test):
        instruction: str = instructions[step]
        if step == 0:
            result = take_step(data.copy(), instruction)
        else:
            take_step(result, instruction)
    # Compare against expectation
    # Load
    test_output_path: Path = INPUT_DIR_PATH / f'test_output_step_{num_test}.txt'
    with open(test_output_path, 'r') as f:
        expectation_raw: str = f.read()
        expectation: ndarray = preprocess_puzzle(expectation_raw)
    # Compare
    assert_check: ndarray = (expectation == result)
    assert_msg: str = f"Test {num_test}) Expectation ({expectation}) != output ({result})!"
    assert assert_check.all(), assert_msg


def test_take_2_steps() -> None:
    # Load data
    with open(TEST_INPUT_PATH, 'r') as f:
        data_raw: str = f.read()
    # Preprocess inputs
    data: ndarray
    instructions: list[str]
    data, instructions = preprocess_inputs(data_raw)
    # Take step
    num_test: int
    result: ndarray
    step: int
    num_test: int = 2
    for step in range(num_test):
        instruction: str = instructions[step]
        result = take_step(data.copy(), instruction) if step == 0 else take_step(result.copy(), instruction)
    # Compare against expectation
    # Load
    test_output_path: Path = INPUT_DIR_PATH / f'test_output_step_{num_test}.txt'
    with open(test_output_path, 'r') as f:
        expectation_raw: str = f.read()
        expectation: ndarray = preprocess_puzzle(expectation_raw)
    # Compare
    assert_check: ndarray = (expectation == result)
    assert_msg: str = f"Test {num_test}) Expectation ({expectation}) != output ({result})!"
    assert assert_check.all(), assert_msg


def test_take_3_steps() -> None:
    # Load data
    with open(TEST_INPUT_PATH, 'r') as f:
        data_raw: str = f.read()
    # Preprocess inputs
    data: ndarray
    instructions: list[str]
    data, instructions = preprocess_inputs(data_raw)
    # Take step
    num_test: int
    result: ndarray
    step: int
    num_test: int = 3
    for step in range(num_test):
        instruction: str = instructions[step]
        result = take_step(data.copy(), instruction) if step == 0 else take_step(result.copy(), instruction)
    # Compare against expectation
    # Load
    test_output_path: Path = INPUT_DIR_PATH / f'test_output_step_{num_test}.txt'
    with open(test_output_path, 'r') as f:
        expectation_raw: str = f.read()
        expectation: ndarray = preprocess_puzzle(expectation_raw)
    # Compare
    assert_check: ndarray = (expectation == result)
    assert_msg: str = f"Test {num_test}) Expectation ({expectation}) != output ({result})!"
    assert assert_check.all(), assert_msg


def test_take_4_steps() -> None:
    # Load data
    with open(TEST_INPUT_PATH, 'r') as f:
        data_raw: str = f.read()
    # Preprocess inputs
    data: ndarray
    instructions: list[str]
    data, instructions = preprocess_inputs(data_raw)
    # Take step
    num_test: int
    result: ndarray
    step: int
    num_test: int = 3
    for step in range(num_test):
        instruction: str = instructions[step]
        result = take_step(data.copy(), instruction) if step == 0 else take_step(result.copy(), instruction)
    # Compare against expectation
    # Load
    test_output_path: Path = INPUT_DIR_PATH / f'test_output_step_{num_test}.txt'
    with open(test_output_path, 'r') as f:
        expectation_raw: str = f.read()
        expectation: ndarray = preprocess_puzzle(expectation_raw)
    # Compare
    assert_check: ndarray = (expectation == result)
    assert_msg: str = f"Test {num_test}) Expectation ({expectation}) != output ({result})!"
    assert assert_check.all(), assert_msg


def main() -> None:
    # Read the top
    test_read_the_top()
    # Take steps
    test_take_step()
    test_take_2_steps()
    test_take_3_steps()
    test_take_4_steps()
    pass


if __name__ == "__main__":
    main()
