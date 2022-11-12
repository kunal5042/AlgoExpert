# https://www.algoexpert.io/questions/sorted-squared-array
# Arrays

'''O(n) Time and O(n) Space'''
def sortedSquaredArray(array):
    # Write your code here.
	result = [0 for _ in array]
	low = 0
	high = len(array) - 1
	for idx in reversed(range(len(array))):
		start = array[low]
		end = array[high]
		
		if abs(start) > abs(end):
			result[idx] = start * start
			low += 1
		else:
			result[idx] = end * end
			high -= 1
	
	return result


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

'''