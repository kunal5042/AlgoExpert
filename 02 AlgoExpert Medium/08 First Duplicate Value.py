# https://www.algoexpert.io/questions/first-duplicate-value
# Arrays

'''
O(n) Time | O(n) Space: Where n is the length of the array
'''
def firstDuplicateValue(array):
	# Algorithm
	# Initialize a hash map to keep track of visited elements
	# While traversing check if the current element has already been visited
	# If not, mark it as visited
	# The first element which is found to be already visited is the result
	visited = {}
	for ele in array:
		if ele in visited:
			return ele
		else:
			visited[ele] = True
	# If not one even one element was repeated
	# result = -1
	return -1

'''O(n) Time and O(1) Space'''
def firstDuplicateValue(array):
    for idx, num in enumerate(array):
        if array[abs(num)-1] < 0:
            return abs(num)

        array[abs(num)-1] *= -1
        
    return -1



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValue(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''