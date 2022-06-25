'''
O(n* 2^n) Time and O(n* 2^n) Space
'''
def powerset(array):
	subsets = [[]]
	
	for ele in array:
		
		for idx in range(len(subsets)):
			current_subset = subsets[idx]
			subsets.append(current_subset + [ele])
		
	return subsets

# Kunal Wadhwa
