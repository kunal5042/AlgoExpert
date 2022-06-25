'''
O(n) Time | O(1) Space: where n is the length of the input array
'''
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

# Kunal Wadhwa
