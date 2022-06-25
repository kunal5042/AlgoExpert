'''
O(n**2) Time | O(1) Space: where n is the length of the input array
'''
def selectionSort(array, reverse=False):
	# Algorithm

	# Virtually split the array into two parts, sorted and unsorted
	# Traverse the unsorted part and find the minimum of all the elements
	# Place this element at the end of the sorted part
	# Perform the above two steps length of the array times

    # this is sorted part's last index + 1th index
    sorted_destination = 0

    for idx in range(len(array)):
        smallest = idx
        # traversing the unsorted part
        for jdx in range(idx, len(array)):
            if reverse is True:
                if array[smallest] < array[jdx]:
                    smallest = jdx
            else:
                if array[smallest] > array[jdx]:
                    smallest = jdx

        # place it at the end of sorted part
        array[sorted_destination], array[smallest] = array[smallest], array[sorted_destination]
        sorted_destination += 1
    
    return array

# Kunal Wadhwa
