import unittest 

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        try:
            print("Test Passed")
            test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
            self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        except:
            print("Test Failed")
        
def zigzagTraverse(array):
    result = []
    height = len(array)    - 1
    width  = len(array[0]) - 1
    (row, col) = (0, 0)
    direction_down = True

    while not out_of_bounds(row, col, height, width):
        result.append(array[row][col])
        if direction_down is True:
            if col == 0 or row == height:
                direction_down = False
                if row == height:
                    # we can't go down any further, move left
                    col += 1
                else:
                    # we can go down, move down
                    row += 1
            else:
                # going down but not at the first column or the last row
                # diagonally go down
                row += 1
                col -= 1

        else:
            # going up
            if row == 0 or col == width:
                # if we are in the top row or the last column
                direction_down = True
                if col == width:
                    # are we in the final column?
                    # we can't go any further towards right, so go down
                    row += 1
                else:
                    # we are in top row and not in last column
                    # go right
                    col += 1
            else:
                # not in top row and nor the last column
                # move up diagonally
                row -= 1
                col += 1

    return result


def out_of_bounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
