'''
O(n) Time | O(1) Space: where n is the length of the input array.
'''
def isMonotonic(array):
	non_increasing, non_decreasing = True, True
	
	for idx in range(1, len(array)):
		prev, curr = array[idx-1], array[idx]
		non_increasing = False if curr > prev else non_increasing
		non_decreasing = False if prev > curr else non_decreasing
	
	# array is monotonic if either of the two is True
	return non_increasing or non_decreasing

# Kunal Wadhwa
