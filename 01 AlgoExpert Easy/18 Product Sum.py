def productSum(array, depth = 1):
    # Write your code here.
	Sum = 0
	for element in array:
		if type(element) is list:
			Sum+= productSum(element, depth + 1)
		else:
			Sum+= element
	return Sum * depth

# Kunal Wadhwa
