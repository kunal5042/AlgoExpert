# https://www.algoexpert.io/questions/first-non-repeating-character
# Strings

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



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter(input)
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