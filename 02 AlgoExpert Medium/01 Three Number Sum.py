def three_num_sum(array, target):
	result = []
	array.sort()
	
	for idx in range(len(array)-2):
		first = idx + 1
		last = len(array) - 1
		
		while first < last:
			potential = array[idx] + array[first] + array[last]
			
			if potential == target:
				new_list = [array[idx], array[first], array[last]]
				result.append(new_list)
				first += 1
				last += -1
				
			elif potential > target:
				last += -1
			else:
				first += 1
	
	return result