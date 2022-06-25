'''
O(log(n)) Time | O(1) Space: where n is the lenght of the sorted input array
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

# Kunal Wadhwa
