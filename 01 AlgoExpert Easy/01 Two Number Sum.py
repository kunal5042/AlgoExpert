# https://www.algoexpert.io/questions/two-number-sum
# Arrays

def twoNumberSum(array, targetSum):
    # Write your code here.
	hash = {}
	result = []
	
	for value in array:
		hash_target = targetSum - value
		if hash_target in hash:
			result.append(value)
			result.append(hash_target)
			return result
		else:
			hash[value] = True
		
	return result



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
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