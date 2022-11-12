# https://www.algoexpert.io/questions/staircase-traversal
# Recursion

def staircaseTraversal(height, maxSteps):
    # to store the number of ways we can reach every step between height (0 to given height)
    ways = [None for x in range(height+1)]
    # base case
    ways[0] = 1
    
    def calculate(current_height):
        # if height is greater, we can stop
        if current_height > height:
            return

        # we don't know the number of ways to reach current_height yet so equal to 0
        current_ways = 0
        '''
        LOGIC:
        ways[h] = ways[h-1] + ways[h-2] + ....... ways[h-k]: where h is the current_height and k is the maxSteps
        '''
        for idx in range(1, maxSteps+1):
            if current_height - idx >= 0:
                current_ways += ways[current_height-idx]

        # store the number of ways for current height
        ways[current_height] = current_ways
        # advance to the next height
        calculate(current_height+1)

    # start with height equals 1
    calculate(1)
    # return the number of ways calculated for the given height
    return ways[-1]




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''