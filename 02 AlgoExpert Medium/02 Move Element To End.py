def moveElementToEnd(array, toMove):
	return move_to_end(array, toMove)

'''
O(n) Time | O(1) Space: where n is the length of the input array
'''
def move_to_end(array, to_move):
	# Algorithm
	# Move all the elements which are not equal to toMove to the front
	# By the end of the traversal all the toMove elements will be at the end 
	# front index = to_put_at
	to_put_at = 0
	for idx in range(len(array)):
		if array[idx] != to_move:
			# if current is not equal to target
			# move current to the front
			array[idx], array[to_put_at] = array[to_put_at], array[idx]
			# new front 
			to_put_at +=1
	return array

# Kunal Wadhwa
