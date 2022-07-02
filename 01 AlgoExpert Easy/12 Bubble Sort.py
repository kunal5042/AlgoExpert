# https://www.algoexpert.io/questions/bubble-sort
# Sorting

def bubbleSort(array, reverse=False):
	# Algorithm
	# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
	# compares adjacent elements and swaps them if they are in the wrong order.
	# The pass through the list is repeated until the list is sorted.
	# The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. 
	'''
	O(n**2) Time | O(1) Space: where n is the length of the input array
	'''
	for idx in range(len(array)):
		sorted = True
		for jdx in range(len(array)-idx-1):
			if reverse is True:
				if array[jdx] < array[jdx+1]:
					array[jdx], array[jdx+1] = array[jdx+1], array[jdx]
					sorted = False
			else:
				if array[jdx] > array[jdx+1]:
					array[jdx], array[jdx+1] = array[jdx+1], array[jdx]
					sorted = False

		if sorted:
			return array



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
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