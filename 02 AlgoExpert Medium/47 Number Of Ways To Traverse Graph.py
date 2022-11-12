# https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph
# Dynamic Programming

'''Dynamic Programming Solution'''
def numberOfWaysToTraverseGraph(width, height):
    # reason for plus 1 is that we don't run into an index error
    # and we don't have to check if x - 1 or y -1 is within bounds for top row and first column
    num_ways = [[0 for _ in range(width+1)] for _ in range(height+1)]

    # loop through all the columns and then all the rows in the columns 
    for width_idx in range(1, width + 1):
        for height_idx in range(1, height + 1):
            if width_idx == 1 or height_idx == 1:
                num_ways[height_idx][width_idx] = 1
            
            else:
                ways_left = num_ways[height_idx][width_idx - 1]
                ways_up   = num_ways[height_idx - 1][width_idx]
                num_ways[height_idx][width_idx] = ways_up + ways_left

    return num_ways[height][width]
    
class GridInfo:
    def __init__(self, ways, width, height):
        self.ways = ways
        self.target_x = width - 1
        self.target_y = height - 1
        self.RC = 0

'''Recursive Solution'''
def numberOfWaysToTraverseGraph(width, height):
    def calculate(direction, x, y):
        if x >= width or y >= height:
            return
        grid_info.RC += 1

            
        if direction == 'right':
            x += 1

        if direction == 'down':
            y += 1

        if x == grid_info.target_x and y == grid_info.target_y:
            grid_info.ways += 1
            return
        calculate('right', x, y)
        calculate('down', x, y)


    grid_info = GridInfo(0, width, height)
    calculate('right', 0, 0)
    calculate('down', 0, 0)
    print(width, height, grid_info.RC)
    return grid_info.ways




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        width = 4
        height = 3
        expected = 10
        actual = numberOfWaysToTraverseGraph(width, height)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''