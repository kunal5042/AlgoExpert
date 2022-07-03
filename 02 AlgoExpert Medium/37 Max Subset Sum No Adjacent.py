# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
# Dynamic Programming

def maxSubsetSumNoAdjacent(array):
    if len(array) <= 2:
        if len(array) == 0:
            return 0
        return max(array)

    dynamic_maxsum = [None] * len(array)
    dynamic_maxsum[0] = array[0]
    dynamic_maxsum[1] = max(array[0], array[1])
    
    for idx in range(2, len(array)):
        dynamic_maxsum[idx] = max(dynamic_maxsum[idx-1], dynamic_maxsum[idx-2] + array[idx])

    return dynamic_maxsum[-1]



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)
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
