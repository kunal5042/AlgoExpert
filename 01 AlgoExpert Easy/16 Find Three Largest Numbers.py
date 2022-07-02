# https://www.algoexpert.io/questions/find-three-largest-numbers
# Searching

'''
O(n*m) Time | O(1) Space: where n is the length of the input array and,
m is the number of largest elements required

Runs in O(n) Time if m is fixed
'''
def get_n_largest(array, number):
	if number > len(array):
		return array
	
	result = [None] * number
	
	for idx in range(number):
		largest = 0
		for arr_idx in range(len(array) - idx):
			if array[arr_idx] > array[largest]:
				largest = arr_idx
		
		array[largest], array[len(array) -1 -idx] = array[len(array) -1 -idx], array[largest]
		result[number -1 -idx] = array[len(array) -1 - idx]
	
	return result
		


def findThreeLargestNumbers(array):
    return get_n_largest(array, 3)




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
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