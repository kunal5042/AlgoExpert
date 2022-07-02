# https://www.algoexpert.io/questions/non-constructible-change
# Arrays

def nonConstructibleChange(coins):
    Change  = 0
    coins.sort()

    for coin in coins:
        if coin > Change + 1:
            return Change + 1
        else:
            Change += coin
    
    return Change + 1

'''
O(nlogn) time | O(1) space - where n is the number of coins
'''



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
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