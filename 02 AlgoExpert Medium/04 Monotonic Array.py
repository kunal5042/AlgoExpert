# https://www.algoexpert.io/questions/monotonic-array
# Arrays

def isMonotonic(array):
	non_increasing, non_decreasing = True, True
	
	for idx in range(1, len(array)):
		prev, curr = array[idx-1], array[idx]
		non_increasing = False if curr > prev else non_increasing
		non_decreasing = False if prev > curr else non_decreasing
	
	# array is monotonic if either of the two is True
	return non_increasing or non_decreasing


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)
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