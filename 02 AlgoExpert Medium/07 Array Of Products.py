# https://www.algoexpert.io/questions/array-of-products
# Arrays

'''O(n) Time and O(n) Space'''
def arrayOfProducts(array):
	return array_of_products(array)

def array_of_products(array):
	# to store the running products from the left and the right
	left_products = [None] * len(array)
	right_products = [None] * len(array)
	# to keep track of running products from the left and the right
	left_p = 1
	right_p = 1
	
	# to store the result
	products = [None] * len(array)
	
	for idx in range(len(array)):
		# fill the array with running products from the left
		left_products[idx] = left_p * array[idx]
		left_p = left_products[idx]
	
	for idx in reversed(range(len(array))):
		# fill the array with running products from the right
		right_products[idx] = right_p * array[idx]
		right_p = right_products[idx]
	
	for idx in range(len(array)):
		result = 1
		if idx-1 >= 0:
			result *= left_products[idx-1]
		if idx+1 < len(array):
			result *= right_products[idx+1]
		products[idx] = result
	# return the result
	return products



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(actual, expected)

        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''