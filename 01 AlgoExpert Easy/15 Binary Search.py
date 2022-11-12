# https://www.algoexpert.io/questions/binary-search
# Searching

'''
O(log(n)) Time | O(1) Space: where n is the length of the sorted input array
'''
def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	
	while left <= right:
		middle = ( left + right ) // 2
		potential_match = array[middle]
		
		if potential_match == target:
			return middle
		
		elif potential_match > target:
			right = middle - 1
		
		else:
			left = middle + 1
			
	return -1



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

'''