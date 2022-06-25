'''
O(n) Time | O(1) Space: where n is the length of the input array
'''
def isValidSubsequence(array, sequence):
	if len(sequence) == 0:
		return True

	idx_sub = 0
	for value in array:
		if value == sequence[idx_sub]:
			idx_sub += 1
			if idx_sub == len(sequence):
				return True

	return False

# Kunal Wadhwa
