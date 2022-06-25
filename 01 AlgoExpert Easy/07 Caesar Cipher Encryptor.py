'''
O(n) Time | O(1) Space: Where n is the length of the input string
'''
def caesarCipherEncryptor(string, key):
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	
	result = ''
	for char in string:
		# Algorithm
		# Find the index of the current character in the list of alphabets
		# Resultant element's index in the alphabets list will be the circular incrementaion of the current character's index
		# Append the new character to the result 
		result += alphabets[ (alphabets.index(char) + key) % 26 ]
	
	return result

# Kunal Wadhwa
