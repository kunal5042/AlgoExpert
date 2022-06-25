'''
O(n) Time | O(n) Space: where n is the length of the input array
'''
def twoNumberSum(array, targetSum):
    # Write your code here.
	hash = {}
	result = []
	
	for value in array:
		hash_target = targetSum - value
		if hash_target in hash:
			result.append(value)
			result.append(hash_target)
			return result
		else:
			hash[value] = True
		
	return result

# Kunal Wadhwa
