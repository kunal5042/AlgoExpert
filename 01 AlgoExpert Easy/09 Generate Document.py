'''
O(n+m) Time | O(c) Space: Where n is the number of the characters, m is the length of the document
                          and c is the number of the unique characters in the characters string
'''
def generateDocument(characters, document):
	# Keeps track of the count of available characters to us
	available = {}
	for char in characters:
		if char not in available:
			available[char] = 0
		
		available[char] += 1
	
	for char in document:
		# If the char we require to generate the document is not available 
		# Return False
		if char not in available or available[char] == 0:
			return False
		
		available[char] -= 1
	
	# If the code reached this statement, that means we have all the characters 
	# we need to generate the document, hence return True
	return True
		
# Kunal Wadhwa
