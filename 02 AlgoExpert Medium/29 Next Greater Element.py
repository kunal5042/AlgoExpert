# https://www.algoexpert.io/questions/next-greater-element
# Stacks

'''
O(n) Time and O(n) Space: where n is the length of the input array
'''
def nextGreaterElement(array):
	result = [-1 for x in array]
	stack = []

	for idx in range(2 * len(array)):
		circular_idx = idx % len(array)
		
		while len(stack):
			top = array[stack[len(stack)-1]]
			ele = array[circular_idx]
			
			if top < ele:
				result[stack.pop()] = ele
				
			else:
				break
				
		stack.append(circular_idx)

	return result



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 5, -3, -4, 6, 7, 2]
        expected = [5, 6, 6, 6, 7, -1, 5]
        actual = nextGreaterElement(input)
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