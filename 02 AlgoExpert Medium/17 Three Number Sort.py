# https://www.algoexpert.io/questions/three-number-sort
# Sorting

'''
O(n) Time | O(1) Space: where n is the length of the input array
'''
def threeNumberSort(array, order):
	# keeps track of frequency of order elements 
	counts = [0, 0, 0]
	for ele in array:
		# updates the frequencies accordingly 
		if ele == order[0]: counts[0] += 1
		if ele == order[1]: counts[1] += 1
		if ele == order[2]: counts[2] += 1
	
	# update the array
	# the idea is to not sort, but update the values in the order as required
	# because there are only finite (3 in this case) types of values/elements
	position = 0
	for _ in range(counts[0]):
		array[position] = order[0]
		position += 1
		
	for _ in range(counts[1]):
		array[position] = order[1]
		position += 1
		
	for _ in range(counts[2]):
		array[position] = order[2]
		position += 1
		
	return array



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
        actual = threeNumberSort(array, order)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''