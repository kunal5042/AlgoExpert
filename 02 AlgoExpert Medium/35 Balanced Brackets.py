import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)
        print("Test Passed")

def balancedBrackets(string):
	return balanced_brackets(string)

def match(open, close):
	if open == '(' and close == ')':
		return True
	if open == '{' and close == '}':
		return True
	if open == '[' and close == ']':
		return True
	return False

def balanced_brackets(string):
	stack = []
	for bracket in string:
		if bracket == '(' or bracket == '{' or bracket == '[':
			stack.append(bracket)
		
		if bracket == ')' or bracket == '}' or bracket == ']':
			if len(stack) == 0:
				return False
			if not match(stack.pop(), bracket):
				return False
	
	if len(stack) == 0:
		return True
	else:
		return False

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
