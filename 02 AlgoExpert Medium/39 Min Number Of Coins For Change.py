# https://www.algoexpert.io/questions/min-number-of-coins-for-change
# Dynamic Programming

# Algorithm
#     - We create a dp array min_coins of length n+1 initialized with FLOAT_MAX
#     - In this array at every index we store the minimum number of coins we need to make amount = this index
#     - We do this by using all the denoms one by one and checking what all amounts we can make using this denom
#     - And how many counts of this denom we are using to make this amount, we keep track of the minimum number of coins we can use to make the current amount
#     - At every step we re-use the result of the sub-problems we solved earlier using our dp array
#     - The base-case is that for amount = 0 we don't need any coin
#     - We build on this result and solve further sub-problems until we reach our result

def minNumberOfCoinsForChange(n, denoms):
    min_coins    = [float('inf') for _ in range(n+1)]
    min_coins[0] = 0

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                min_coins[amount] = min(min_coins[amount-denom]+1, min_coins[amount])

    return min_coins[-1] if min_coins[-1] != float('inf') else -1
    


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 5, 10]), 3)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''