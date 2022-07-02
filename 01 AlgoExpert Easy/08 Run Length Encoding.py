# https://www.algoexpert.io/questions/run-length-encoding
# Strings

'''
O(n) Time | O(1) Space: Where n is the length of the input string
'''
def encode(count, char, result):
	if count > 9:
		wraps = count // 9
		remaining = count % 9
		for _ in range(wraps):
			result[0] += '9' + char
		result[0] += str(remaining) + char
	else:
		result[0] += str(count) + char
	
def runLengthEncoding(string):
	result = ['']
	# Holds the char that we will try to match with array elements to find it's frequency
	buffer = string[0]
	# Frequency of the buffer
	count = 0
	
	for char in string:
		if char == buffer:
			# Increment the frequency
			count += 1
		else:
			# The current character has appeared count times till now
			# We can safely encode it now
			encode(count, buffer, result)
			# Our current character is the new buffer element and it's frequency so far is 1
			buffer = char
			count = 1
	# Last set of matching characters are still in buffer and have not yet been added to the result
	encode(count, buffer, result)
	# Return the result
	return result[0]



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = runLengthEncoding(string)
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