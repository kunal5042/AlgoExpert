# https://www.algoexpert.io/questions/insertion-sort
# Sorting

def insertionSort(array, reverse=False):
	# Algorithm

	# Virtually split the array into two parts, sorted and unsorted
	# Pick the first element from the unsorted part
	# Place this element at the correct position in the sorted part (inserting into sorted part, this is where the name came from)
	# Perform the above two operations until all the elements from the unsorted part are brought into the sorted part

	'''
	O(n**2) Time | O(1) Space: where n is the length of the input array
	'''
	for idx1 in range(1, len(array)):
		for idx2 in reversed(range(idx1)):
			if reverse:
				if array[idx1] > array[idx2]:
					array[idx1], array[idx2] = array[idx2], array[idx1]
					idx1 -= 1
				else:
					break
			else:
				if array[idx1] < array[idx2]:
					array[idx1], array[idx2] = array[idx2], array[idx1]
					idx1 -= 1
				else:
					break
	return array



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
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