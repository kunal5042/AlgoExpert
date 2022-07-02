# https://www.algoexpert.io/questions/nth-fibonacci
# Recursion

'''
O(n) Time | O(n) Space
'''
def getNthFib(n, memoize={1:0, 2:1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
		return memoize[n]



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(6), 5)

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