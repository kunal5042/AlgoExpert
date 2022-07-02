# https://www.algoexpert.io/questions/validate-subsequence
# Arrays

'''O(n) Time and O(1) Space'''
def isValidSubsequence(array, sequence):
    if len(sequence) == 0: return True

    idx_sub = 0
    for value in array:
        # if a matching value is found, increment the index
        if value == sequence[idx_sub]:
            idx_sub += 1

            # if at any step in the traversal of the array
            # we reach the end of the sequence
            # we can stop, and return True
            if idx_sub == len(sequence):
                return True

    if idx_sub == len(sequence):
        return True
    # if we didn't return True by the end of the traversal
    # we can safely return False
    return False



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))
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