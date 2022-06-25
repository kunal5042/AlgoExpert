'''
O(n*I) Time | O(c) Space: where n is the number of words, I is the length of the longest word and c
is the number of unique characters in across all words
'''
def minimumCharactersForWords(words):
	result = []
	min_frequencies = {}
	
	for word in words:
		# characters required to generate the current word
		characters = {}
		for char in word:
			characters[char] = characters.get(char, 0) + 1
			# minimum of current character required = frequency of current character required in the word
			# which requires the maximum frequency of current character
			min_frequencies[char] = max(min_frequencies.get(char, 0), characters[char])
	
	# generating resultant array from the dictionary 
	for key, value in min_frequencies.items():
		for _ in range(value):
			result.append(key)
			
	return result

# Kunal Wadhwa
