'''
Best    : O(n) Time and O(1) Space
Average : O(n) Time and O(1) Space
Worst   : O(n^2) Time and O(1) Space
'''
def quickselect(array, k):
    def helper(start, end, position):
        while True:
            if start > end:
                raise Exception("Your algorithm should never arrive here!")

            pivot = start
            left  = pivot + 1
            right = end

            # quick-sort logic
            while left <= right:
                if array[left] > array[pivot] and array[right] < array[pivot]:
                    # swap
                    swap(left, right)

                if array[left] <= array[pivot]:
                    left += 1

                if array[right] >= array[pivot]:
                    right -= 1

            # left surpassed right
            swap(pivot, right)


            # quick-select logic
            if right == position:
                return array[right]

            elif right < position:
                # discard the entire left part
                start = right + 1
            else:
                # discard the entire right part
                end = right - 1

    def swap(x, y):
        array[x], array[y] = array[y], array[x]

    return helper(0, len(array)-1, k-1)

'''
Forms a geometric series which converges to 2n.
Hence the complexity is O(n)
'''

'''
Main Idea:
Put one element in it's correct position by putting all elements smaller to it, to it's left and all elements greater to it, to it's right.
Now using the information of this correctly positioned element.
Determine in which half i.e left or right half the required element must exist in.

Algorithm:
    - Start with the first index as the pivot of the current array with starting index = start and ending index = end
    - Shift all the greater elements to it's right and smaller to it's left
    - Put pivot in it's correct position, and let's call it pivot_index
    - Compare the pivot_index with position
    - if pivot_index == position:
        we found the kth smallest element
        reasoning: this element is in it's correct position because of the nature of computation we did earlier

    - if pivot_index < position:
        we move back to step 1, but this time we discard the entire left part when we search for smaller and greater elements
        so, new start = pivot_index + 1
        reasoning: all the elements towards the left of the pivot_index are smaller than pivot and pivot_index itself is smaller than the position.
        hence the element that will fit in the position we are looking for has to be greater than all those elements and should be present in the right part.

    - if pivot_index > position:
        we move back to step 1, but this time we discard the entire right part when we search for smaller and greater elements
        so, new end = pivot_index - 1
        reasoning: the element that fits in the position we are looking for has to be present in the left part. As it must be smaller than the pivot element.
        because, pivot is in it's correct position
'''


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickselect([8, 5, 2, 9, 7, 6, 3], 3), 5)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa