import unittest
import numpy as np

def quickSort(array):
	quick_sort_recur(array, 0, len(array)-1)
	return array

def quick_sort_recur(array, start_idx, end_idx):
	# base case
	if start_idx >= end_idx:
		return
	
	pivot_idx = start_idx
	left	  = start_idx + 1
	right	  = end_idx
	
	while right >= left:
		(lower, pivot, upper) = (array[left], array[pivot_idx], array[right])
		
		if lower > pivot and upper < pivot:
			swap(left, right, array)
			
		if lower <= pivot:
			left += 1
			
		if upper >= pivot:
			right -= 1
			
	swap(pivot_idx, right, array)
	
	is_smaller = {'left subarray': False, 'right subarray': False}
	
	if right - 1 - start_idx < end_idx - (right + 1):
		is_smaller['left subarray'] = True
	else:
		is_smaller['right subarray'] = True
		
	if is_smaller['left subarray'] is True:
		quick_sort_recur(array, start_idx, right - 1)
		quick_sort_recur(array, right + 1, end_idx)
		
	if is_smaller['right subarray'] is True:
		quick_sort_recur(array, right + 1, end_idx)
		quick_sort_recur(array, start_idx, right - 1)
		
def swap(source, destination, array):
	array[source], array[destination] = array[destination], array[source]

# Test Framework
class TestProgram(unittest.TestCase):
    def test_case_1(self, array, sorted_array):
        self.assertEqual(quickSort(array), sorted_array, 'Not sorted properly')
        
def run_tests(run, count, array_size, array_range_lower, array_range_upper):
    for test_case_count in range(1,count+1):
        # create a random array of size from 0 to array_size
        size_array = np.random.randint(0, array_size)
        array = []
        for _ in range(size_array):
            array.append(np.random.randint(array_range_lower, array_range_upper))
            
        # array is generated, let's send it to the test program
        sorted_array = sorted(array)
        
        # send for the testing
        try:
            run.test_case_1(array, sorted_array)
            print(f'Test Case {test_case_count}: Passed\nINPUT: {array}\n')
        except:
            print(f'Test Case {test_case_count}: Failed\nINPUT: {array}\n')
    
if __name__ == "__main__":
    run = TestProgram()
    run_tests(run, 25, 10, -50, 100)

            
# Kunal Wadhwa
