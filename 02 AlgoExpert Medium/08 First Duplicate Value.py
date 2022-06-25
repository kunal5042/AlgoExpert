'''
O(n) Time | O(n) Space: Where n is the length of the array
'''
def firstDuplicateValue(array):
	# Algorithm
	# Initialize a hash map to keep track of visited elements
	# While traversing check if the current element has already been visited
	# If not, mark it as visited
	# The first element which is found to be already visited is the result
	visited = {}
	for ele in array:
		if ele in visited:
			return ele
		else:
			visited[ele] = True
	# If not one even one element was repeated
	# result = -1
	return -1

# Kunal Wadhwa
