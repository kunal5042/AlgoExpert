import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)
        print('Test Case: Passed')


'''O(n) T and O(n) S: where n is the length of the input array'''
def maxSubsetSumNoAdjacent(array):
    if len(array) <= 2:
        if len(array) == 0:
            return 0
        return max(array)

    dynamic_maxsum = [None] * len(array)
    dynamic_maxsum[0] = array[0]
    dynamic_maxsum[1] = max(array[0], array[1])
    result_sum = float('-inf')
    
    for idx in range(2, len(array)):
        dynamic_maxsum[idx] = max(dynamic_maxsum[idx-1], dynamic_maxsum[idx-2] + array[idx])

    return dynamic_maxsum[-1]

'''O(n) T and O(1) S: where n is the length of the input array'''
def maxSubsetSumNoAdjacentEfficient(array):
    if len(array) == 0:
        return 0

    if len(array) <= 2:
        return max(array)

    idx_minus_two = array[0]
    idx_minus_one = max(array[0], array[1])
    result        = float('-inf')
    
    for idx in range(2, len(array)):
        result = max(idx_minus_one, idx_minus_two + array[idx])

        idx_minus_two = idx_minus_one
        idx_minus_one = result

    return result

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa

