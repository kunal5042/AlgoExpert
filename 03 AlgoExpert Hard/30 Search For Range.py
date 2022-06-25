'''
O(log(n)) Time and O(1) Space
'''
def searchForRange(array, target):
    left, right = 0, len(array)-1
    left_extreme, right_extreme = None, None
    
    while left <= right:
        middle = (left + right)// 2
        if array[middle] == target:
            if middle == 0 or array[middle-1] != target:
                left_extreme = middle
                break
            else:
                right = middle - 1
            continue

        if array[middle] > target:
            right = middle - 1

        else:
            left = middle + 1


    left, right = 0, len(array)-1
    while left <= right:
        middle = (left + right)// 2
        if array[middle] == target:
            if middle == len(array)-1 or array[middle+1] != target:
                right_extreme = middle
                break
            else:
                left = middle + 1
            continue

        if array[middle] > target:
            right = middle - 1

        else:
            left = middle + 1

    if left_extreme is None or right_extreme is None:
        return [-1, -1]

    return [left_extreme, right_extreme]
    
            
                


'''
Given    : Sorted array of integers
Goal     : Find range of indices in the input array in which we can find the target number at every index
Expected : O(log(n))

Idea     : Do Binary-Search twice, and find the left and right extremes for the given target
'''

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4, 9])
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
