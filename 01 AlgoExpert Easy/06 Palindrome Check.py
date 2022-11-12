# https://www.algoexpert.io/questions/palindrome-check
# Strings

'''
O(n) Time | O(1) Space: Where n is the length of the input string
'''
def isPalindrome(string):
	left, right = 0, len(string) - 1
	
	while left <= right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	
	return True



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(isPalindrome("abcdcba"), True)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

'''