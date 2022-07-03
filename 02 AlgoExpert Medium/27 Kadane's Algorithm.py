# https://www.algoexpert.io/questions/kadane's-algorithm
# Famous Algorithms

'''O(n) Time and O(1) Space'''
def kadanesAlgorithm(array):
    # Write your code here.
    dynamic_sum = array[0]
    result      = dynamic_sum

    for idx in range(1, len(array)):
        num         = array[idx]
        dynamic_sum = max(dynamic_sum + num, num)
        result      = max(result, dynamic_sum)

    return result
    


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)
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