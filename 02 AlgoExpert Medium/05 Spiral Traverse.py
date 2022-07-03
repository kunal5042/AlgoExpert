# https://www.algoexpert.io/questions/spiral-traverse
# Arrays

def spiralTraverse(array):
	spiral_traversal = []
	
	increasing_row, increasing_col = 0, 0
	decreasing_row, decreasing_col = len(array) - 1, len(array[0]) - 1
	
	while increasing_row <= decreasing_row and increasing_col <= decreasing_col:
		for col in range(increasing_col, decreasing_col + 1):
			spiral_traversal.append(array[increasing_row][col])
			
		for row in range(increasing_row + 1, decreasing_row + 1):
			spiral_traversal.append(array[row][decreasing_col])
			
		for col in reversed(range(increasing_col, decreasing_col)):
			if increasing_row == decreasing_row:
				break
			spiral_traversal.append(array[decreasing_row][col])
		
		for row in reversed(range(increasing_row + 1, decreasing_row)):
			if increasing_col ==  decreasing_col:
				break
			spiral_traversal.append(array[row][increasing_col])
		
		increasing_col += 1
		decreasing_col -= 1
		increasing_row += 1
		decreasing_row -= 1
	
	return spiral_traversal
    


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''