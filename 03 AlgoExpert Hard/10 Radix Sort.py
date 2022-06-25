import unittest

'''
O(d *(n+b)) T and O(n+b) S: where n is the length of the input array
                            d is the max number of digits
                            b is the base of the number system used

Best Case: O(n) linear

Can perform more efficiently than Quick Sort, Heap Sort and Merge Sort in some cases.

Advantages of Radix Sort
- Fast when the keys are short i.e. when the range of the array elements is less.
- Used in suffix array constuction algorithms like Manber's algorithm and DC3 algorithm.
- Radix Sort is stable sort as relative order of elements with equal values is maintained.

NOTE: This implementation works for only positive numbers :)
'''

def radixSort(array):
    if len(array) == 0:
        return array

    largest_number = max(array)

    digit = 0
    # if the maximum number in the array divided by 10 to the power of number of digits processed is greater than 0
    # we still have more digits to process
    # otherwise, sorting is complete and we can stop
    while largest_number / (10 ** digit) > 0:
        # in place sorting by using counting sort as base
        counting_sort(array, digit)
        digit += 1

    # return sorted array
    return array

def counting_sort(array, digit):
    sorted_array = [0 for _ in range(len(array))]
    # because for every column, the digits we can have can only exist between the range of 0-9 inclusive
    count_array  = [0 for _ in range(10)]

    # our divisor to extract the digit
    digit_column = 10 ** digit

    for number in array:
        # extract the digit and calculate the index in the count_array
        count_index = (number // digit_column) % 10
        # initialized to 0, increment because we found an element whose current column equals the index
        count_array[count_index] += 1

    # now we have all the accurate counts
    # 
    # here, we have updated the furtherst right indices of where we should place numbers that have at those digits
    for index in range(1, 10):
        count_array[index] += count_array[index - 1]

    # we have positions
    # insert numbers in the sorted_array
    # stable sort aspect: reverse traversal
    # we do this in reverse because first matching number is placed at the higher index
    # but, the array is already sorted from the previous stage
    # and to maintain that order, we traverse in reverse
    for index in range(len(array)-1, -1, -1):
        count_index = (array[index] // digit_column) % 10
        # because count_array tells the position and not the index
        count_array[count_index] -= 1
        # after subtracting, it now tells us the index
        sorted_index = count_array[count_index]
        # put the number in the sorted array, based on it's column of digit
        sorted_array[sorted_index] = array[index]

    # copying the sorted array in the actual array 
    # for the next stage of processing
    for index in range(len(array)):
        array[index] = sorted_array[index]
        
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
        expected = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
        actual = radixSort(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
