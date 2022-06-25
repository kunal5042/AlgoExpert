def bubbleSort(array, reverse=False):
	# Algorithm
	# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
	# compares adjacent elements and swaps them if they are in the wrong order.
	# The pass through the list is repeated until the list is sorted.
	# The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. 
	'''
	O(n**2) Time | O(1) Space: where n is the length of the input array
	'''
	for idx in range(len(array)):
		sorted = True
		for jdx in range(len(array)-idx-1):
			if reverse is True:
				if array[jdx] < array[jdx+1]:
					array[jdx], array[jdx+1] = array[jdx+1], array[jdx]
					sorted = False
			else:
				if array[jdx] > array[jdx+1]:
					array[jdx], array[jdx+1] = array[jdx+1], array[jdx]
					sorted = False

		if sorted:
			return array

# Kunal Wadhwa
