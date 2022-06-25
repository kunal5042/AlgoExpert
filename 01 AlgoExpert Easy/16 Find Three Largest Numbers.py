'''
O(n*m) Time | O(1) Space: where n is the length of the input array and,
m is the number of largest elements required

Runs in O(n) Time if m is fixed
'''
def get_n_largest(array, number):
	if number > len(array):
		return array
	
	result = [None] * number
	
	for idx in range(number):
		largest = 0
		for arr_idx in range(len(array) - idx):
			if array[arr_idx] > array[largest]:
				largest = arr_idx
		
		array[largest], array[len(array) -1 -idx] = array[len(array) -1 -idx], array[largest]
		result[number -1 -idx] = array[len(array) -1 - idx]
	
	return result
		


def findThreeLargestNumbers(array):
    return get_n_largest(array, 3)


# Kunal Wadhwa
