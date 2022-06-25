'''
O(log(n)) Time and O(1) Space
'''
def shiftedBinarySearch(array, target):
    left, right = 0, len(array)-1

    while left <= right:
        middle = (left + right)//2

        if array[middle] == target:
            return middle

        if array[left] <= array[middle]:
            # Sorted part
            if target >= array[left] and target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1

        else:
            # left part is unsorted
            # so, right part must be sorted
            # check if the element is present in the sorted part
            if target <= array[right] and target > array[middle]: 
                left = middle + 1
            else:
                right = middle - 1

    return -1

'''
The Idea:
At every iteration,
We split the array into two parts
    - one part is sorted
    - one part is not

We check if the target element is present in the sorted part
    if it's present
        - we search in that part
    else
        - we decrease the unsorted part's length by one
'''

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33), 8)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
