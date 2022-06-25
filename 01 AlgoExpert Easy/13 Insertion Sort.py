def insertionSort(array, reverse=False):
	# Algorithm

	# Virtually split the array into two parts, sorted and unsorted
	# Pick the first element from the unsorted part
	# Place this element at the correct position in the sorted part (inserting into sorted part, this is where the name came from)
	# Perform the above two operations until all the elements from the unsorted part are brought into the sorted part

	'''
	O(n**2) Time | O(1) Space: where n is the length of the input array
	'''
	for idx1 in range(1, len(array)):
		for idx2 in reversed(range(idx1)):
			if reverse:
				if array[idx1] > array[idx2]:
					array[idx1], array[idx2] = array[idx2], array[idx1]
					idx1 -= 1
				else:
					break
			else:
				if array[idx1] < array[idx2]:
					array[idx1], array[idx2] = array[idx2], array[idx1]
					idx1 -= 1
				else:
					break
	return array
 
# Kunal Wadhwa
