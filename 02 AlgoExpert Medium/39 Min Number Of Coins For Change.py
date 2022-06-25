import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 5, 10]), 3)
        print("Test Case: Passed")
        
def minNumberOfCoinsForChange(n, denoms):
    min_coins    = [float('inf') for _ in range(n+1)]
    min_coins[0] = 0

    for denom in denoms:
        for target_amount in range(1, len(min_coins)):
            if denom <= target_amount:
                min_coins[target_amount] = min( min_coins[target_amount], 1 + min_coins[target_amount-denom])
    
    return min_coins[-1] if min_coins[-1] != float('inf') else -1
    
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
