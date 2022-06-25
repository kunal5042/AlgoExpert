'''
O(n) Time | O(1) Space: Where n is the length of the input string
'''
def firstNonRepeatingCharacter(string):
	# Keeps track of the frequencies of the characters appearing in the input string
	frequencies = {}
	for char in string:
		if char not in frequencies:
			frequencies[char] = 0
		
		frequencies[char] += 1
	
	for idx in range(len(string)):
		# The first character in the input string whose frequency is 1
		# That is, it doesn't repeat more than once
		# index of that character is the result
		if frequencies[string[idx]] == 1:
			return idx
	
	# If all the characters are appearing more than once in the input string
	# result = -1
	return -1

# Kunal Wadhwa
