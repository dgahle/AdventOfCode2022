# Imports
from numpy import arange, array, concatenate, ndarray, zeros
from pathlib import Path
from re import match
from typing import Optional


# Variables
REPO_PATH: Path = Path(__file__).parent.parent.parent.parent
INPUT_PATH: Path = REPO_PATH / 'input' / 'day_5' / 'input.txt'


# Functions
def row_to_row_of_cells(row: str, num_cells: int) -> list[str]:
    row_out: list[str] = []
    n_cell: int
    len_cell: int = 3
    lhs_index: int = 0
    for n_cell in range(num_cells):
        rhs_index: int = lhs_index + len_cell
        cell_slice: slice = slice(lhs_index, rhs_index)
        cell: str = row[cell_slice]
        row_out.append(cell)
        lhs_index += 1 + len_cell

    return row_out


def preprocess_puzzle(data: str) -> ndarray:
    # raw data to lines
    lines: list[str] = data.split('\n')
    # process rows to columns
    num: str
    columns_nums: list[int] = [int(num) for num in lines[-1].split('  ')]
    num_columns: int = max(columns_nums)
    # len row = num_columns * 3 + (num_columns - 1)
    #
    row: str
    lines: list[list[str]] = [row_to_row_of_cells(row, num_cells=num_columns) for row in lines[:-1]]
    # rows to columns
    matrix: ndarray = array(lines)
    # Standardise empty cells
    i: int
    empty_cell: str = ''
    for i in range(3):
        i += 1
        empty_space: str = ' '*i
        check: ndarray = (empty_space == matrix)
        matrix[check] = empty_cell

    return matrix


def preprocess_inputs(data: str) -> tuple[ndarray, list[str]]:
    # Separate data and instructions
    data: str
    instructions: str
    separator: str = '\n\n'
    data, instructions = data.split(sep=separator)
    # process data
    data: ndarray = preprocess_puzzle(data)
    # process instructions
    separator: str = '\n'
    instructions: list[str] = instructions.split(sep=separator)
    # Return
    return data, instructions


def read_the_top(data: ndarray) -> str:
    """

    :param data:
    :return:
    """
    n_rows: int
    n_cols: int
    n_rows, n_cols = data.shape
    top_row: list[str] = []
    i_col: int
    cell: str
    for i_col in range(n_cols):
        row: ndarray = data[:, i_col]
        for cell in row:
            if match(r'\[\w]', cell):
                top_row.append(cell[1:-1])
                break
    # Sum
    top_row: str = ''.join(top_row)
    return top_row


def take_step(data: ndarray, instruction: str) -> ndarray:
    # Get parameters of data
    num_rows: int
    num_cols: int
    num_rows, num_cols = data.shape
    # Format string instruction to int
    instruction: ndarray = array(instruction.split(' '))[1 + 2 * arange(3)]
    num_move, col_from, col_to = instruction.astype(int).tolist()
    # Index correction (starts at 1 -> starts at 0)
    index_correction: int = -1
    col_from += index_correction
    col_to += index_correction
    # Get cell(s) to move
    empty_cell: str = ''
    cell_lhs_index: int = max([0, (empty_cell == data[:, col_from]).sum()])
    cell_rhs_index: int = cell_lhs_index + num_move
    cell_index: slice = slice(cell_lhs_index, cell_rhs_index)
    cell_from_index: tuple[slice, int] = (cell_index, col_from)
    cells: ndarray = data[cell_from_index].copy()
    data[cell_from_index] = empty_cell
    # Add cell to new place
    cell_lhs_index: int = max([0, (empty_cell == data[:, col_to]).sum() - 1])
    cell_rhs_index: int = cell_lhs_index + num_move
    cell_index: slice = slice(cell_lhs_index, cell_rhs_index)
    cell_to_index: tuple[slice, int] = (cell_index, col_to)
    # Check if data needs to be expanded
    num_rows_to_add: int = cell_index.stop - num_rows
    if num_rows_to_add > 0:
        # Build missing rows
        shape: tuple[int, int] = (num_rows_to_add, num_cols)
        extra_rows: ndarray = zeros(shape, dtype=str)
        # Add addition rows
        arrays: tuple[ndarray, ndarray] = (extra_rows, data)
        data = concatenate(arrays, axis=0)
        # Update date
        cell_rhs_index: int = max([0, (empty_cell == data[:, col_to]).sum()])
        cell_lhs_index: int = cell_rhs_index - num_move
        cell_index: slice = slice(cell_lhs_index, cell_rhs_index)
        cell_to_index: tuple[slice, int] = (cell_index, col_to)
        data[cell_to_index] = cells[::-1]
    else:
        data[cell_to_index] = cells
    # Check for empty rows
    zero_row_check: Optional[ndarray, bool] = data.shape[1] == (zeros(data.shape[1], dtype=str) == data).sum(1)
    data = data[~zero_row_check]
    return data


def main() -> None:
    pass


if __name__ == "__main__":
    main()
