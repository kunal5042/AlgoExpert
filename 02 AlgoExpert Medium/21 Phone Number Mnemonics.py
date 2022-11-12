# https://www.algoexpert.io/questions/phone-number-mnemonics
# Recursion

'''O(4^n * n) time | O(4^n * n) space - where n is the length of the phone number'''
def phoneNumberMnemonics(phone_number):
	result = []
	hash = {
		'1': '1',    '2': 'abc',   '3': 'def', 
		'4': 'ghi',  '5': 'jkl',   '6': 'mno',
		'7': 'pqrs', '8': 'tuv',   '9': 'wxyz',
					 '0': '0'
	}
	
	def helper(current, mnemonic):
		if len(current) == 0:
			result.append(mnemonic)
			return
		
		number  = current[0]
		current = current[1:]
		
		combinations = hash[number]
		for next_num in combinations:
			helper(current, mnemonic + next_num)
	
	helper(phone_number, "")
	return result
		


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        phoneNumber = "1905"
        expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
        actual = phoneNumberMnemonics(phoneNumber)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''