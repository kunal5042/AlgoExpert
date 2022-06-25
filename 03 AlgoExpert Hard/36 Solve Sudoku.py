def solveSudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def is_valid(value, row, col, board):
    row_is_valid = value not in board[row]
    col_is_valid = value not in map(lambda r: r[col], board)
    if not row_is_valid or not col_is_valid: return False

    subgrid_row_start = row // 3
    subgrid_col_start = col // 3
    for rowidx in range(3):
        for colidx in range(3):
            rowtocheck = subgrid_row_start * 3 + rowidx
            coltocheck = subgrid_col_start * 3 + colidx
            existing_value = board[rowtocheck][coltocheck]

            if existing_value == value:
                return False


    return True



def solve_partial_sudoku(row, col, board):
    currentrow = row
    currentcol = col

    if currentcol == len(board[row]):
        currentrow += 1
        currentcol = 0
        if currentrow == len(board):
            return True


    if board[currentrow][currentcol] == 0:
        return try_digit_at_pos(currentrow, currentcol, board)

    return solve_partial_sudoku(currentrow, currentcol+1, board)



def try_digit_at_pos(row, col, board):
    for digit in range(1, 10):
        if is_valid(digit, row, col, board):
            board[row][col] = digit
            if solve_partial_sudoku(row, col+1, board):
                return True

    board[row][col] = 0
    return False


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]
        expected = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7],
        ]
        actual = solveSudoku(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
