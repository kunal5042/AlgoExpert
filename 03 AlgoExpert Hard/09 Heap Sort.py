import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(heapSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
        print("Test Case: Passed")

def heapSort(array):
    def sift_down(start, end):
        child_one_idx = 2*start + 1
    
        while child_one_idx <= end:
            child_two_idx = 2*start + 2 if 2*start + 2 <= end else -1
    
            if child_two_idx != -1 and array[child_two_idx] > array[child_one_idx]:
                potential_swap_idx = child_two_idx
            else:
                potential_swap_idx = child_one_idx
    
            if array[start] < array[potential_swap_idx]:
                array[start], array[potential_swap_idx] = \
                array[potential_swap_idx], array[start]
    
                start = potential_swap_idx
                child_one_idx = 2*start + 1
            else:
                break
        return
            
    def build_max_heap():
        first_parent = (len(array) - 2) // 2
        for parent in reversed(range(first_parent+1)):
            sift_down(parent, len(array)-1)
        return

    def perform_sorting():
        swap_last = len(array) - 1
        while swap_last != 0:
            array[0], array[swap_last] = array[swap_last], array[0]
            swap_last -= 1
            sift_down(0, swap_last)
        return
        
    build_max_heap()
    perform_sorting()
    return array

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa

