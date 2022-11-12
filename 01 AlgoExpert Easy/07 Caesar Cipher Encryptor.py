# https://www.algoexpert.io/questions/caesar-cipher-encryptor
# Strings

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



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

'''