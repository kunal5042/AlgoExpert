def groupAnagrams(words):
	# words will be stored after arranging them in alphabetical order
	arranged = {}
	for word in words:
		key = "".join(sorted(word))
		if key in arranged:
			# This means this word belongs to sorted(word) group of anagram
			# So, we will add it to that group
			arranged[key].append(word)
		else:
			# This word is the founder of it's group of anagram
			arranged[key] = [word]
	
	return list(arranged.values())

# Kunal Wadhwa
