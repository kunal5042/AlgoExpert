def kadanesAlgorithm(array):
	max_sub_sum = array[0]
	dynamic_sum = array[0]
	
	for idx in range(1, len(array)):
		dynamic_sum = max(array[idx], dynamic_sum + array[idx])
		max_sub_sum = max(dynamic_sum, max_sub_sum)
		
	return max_sub_sum

# Kunal Wadhwa
