# https://www.algoexpert.io/questions/search-in-sorted-matrix
# Sorting

'''
O(n+m) Time | O(1) Space: where n is the length of the matrix's rows and,
m is the length of the matrix's columns
'''
def searchInSortedMatrix(matrix, target):
	if len(matrix) == 0:
		return [-1, -1]
	
	row_no = 0
	col_no = len(matrix[0]) - 1
	
	while row_no >= 0 and row_no < len(matrix) and col_no >= 0 and col_no < len(matrix[0]):
		potential = matrix[row_no][col_no]
		
		if potential > target:
			col_no -= 1
		
		elif potential < target:
			row_no += 1
		
		else:
			return [row_no, col_no]
	
	return [-1, -1]



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 44)
        self.assertEqual(actual, [3, 3])
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