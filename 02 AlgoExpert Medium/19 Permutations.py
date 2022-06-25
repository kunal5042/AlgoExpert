'''
O(n*n!) Time | O(n*n!) Space
'''
def getPermutations(array):
    # Write your code here.
	permutations = []
	helper(array, [], permutations)
	return permutations

def helper(array, cur_perm, perms):
	# if there are no elements from array to append and create a new perm
	# and cur_perm is not empty
	if len(array) == 0 and len(cur_perm) != 0:
		perms.append(cur_perm)
		
	else:
		for pop_index in range(len(array)):
			# remove the element at the pop_index 
			# create a new perm with that element 
			# send the remaining array and new permutation to helper
			# to do  this recursively 
			# until the array is empty and the permutation is complete 
			remaining_array = array[:pop_index] + array[pop_index + 1:]
			new_perm = cur_perm + [array[pop_index]]
			
			helper(remaining_array, new_perm, perms)
			
# Kunal Wadhwa
