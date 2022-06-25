import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)
        print("Test Case: Passed")
        
def numberOfWaysToMakeChange(n, denoms):
    ways    = [0 for _ in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, len(ways)):
            if denom <= amount:
                ways[amount] += ways[amount-denom]

    return ways[-1]

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
