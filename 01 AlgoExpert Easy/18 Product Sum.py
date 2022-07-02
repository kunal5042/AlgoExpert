# https://www.algoexpert.io/questions/product-sum
# Recursion

def productSum(array, depth = 1):
    # Write your code here.
	Sum = 0
	for element in array:
		if type(element) is list:
			Sum+= productSum(element, depth + 1)
		else:
			Sum+= element
	return Sum * depth



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)
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