# https://www.algoexpert.io/questions/minimum-characters-for-words
# Strings

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



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["this", "that", "did", "deed", "them!", "a"]
        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
        actual = minimumCharactersForWords(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''