# https://www.algoexpert.io/questions/number-of-ways-to-make-change
# Dynamic Programming

# Algorithm
#     - We create a new array of length n + 1 initialized with zeroes
#     - At every index of this array we store the the number of ways we can make the change for amount = this index from the denoms available
#     - We build this array with one denomination at a time
#     - One key concept is that say for a given amount X and a denom Y, if we subtract Y from X
#     - The number of ways we can make X can be incremented if we know how many ways we can make X-Y
#     - Since Y + (X-Y) = X: if we want to know how many combinations we can make which will sum upto X
#     - We need to know how many ways can we make (X-Y)
#     - We check our ways array to see how many ways we can make (X-Y)
#     - And, we build this array for all amounts from 0 to n, one denom at a time

def numberOfWaysToMakeChange(n, denoms):
    ways    = [0 for _ in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, len(ways)):
            if denom <= amount:
                ways[amount] += ways[amount-denom]

    return ways[-1]




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)
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