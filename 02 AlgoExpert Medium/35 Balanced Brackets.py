# https://www.algoexpert.io/questions/balanced-brackets
# Stacks

def match(open, close):
	if open == '(' and close == ')':
		return True
	if open == '{' and close == '}':
		return True
	if open == '[' and close == ']':
		return True
	return False

def balancedBrackets(string):
	stack = []
	for bracket in string:
		if bracket == '(' or bracket == '{' or bracket == '[':
			stack.append(bracket)
		
		if bracket == ')' or bracket == '}' or bracket == ']':
			if not len(stack) or not match(stack.pop(), bracket):
				return False
	
	if len(stack) == 0:
		return True
	return False

    


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''