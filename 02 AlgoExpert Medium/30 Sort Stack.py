# https://www.algoexpert.io/questions/sort-stack
# Stacks

def sortStack(stack):
	if len(stack):
		# pop out all the elements until the stack is empty
		popped = stack.pop()
		
		# the call down below will recursively keep popping until the stack is empty
		sortStack(stack)
		# once the stack is empty the call down below will be executed for the first time
		# and it will insert the first element in the stack
		# after that call it will keep inserting all the poppped elements 
		# one after the other in sorted order
		# until all of the elements are inserted
		insert(stack, popped)
		
		# stack will be sorted after all the calls
		# hence return the sorted stack
		return stack
	
	return stack
	


def insert(stack, ele):
	if len(stack) == 0:
		# stack is empty, no sorted order to maintain
		stack.append(ele)
		return
	# if stack top is smaller than element to insert, push it else
	# remove it from the top and recursively call the insert again 
	# until stack top is smaller than the element to insert
	# once you find that stage
	# insert the element
	# and in all the return back calls, insert back all the stack tops popped so far
	popped = stack.pop()
	if ele > popped:
		stack.append(popped)
		stack.append(ele)
		return
	else:
		insert(stack, ele)
	stack.append(popped)
	


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, 2, -2, 4, 3, 1]
        expected = [-5, -2, 1, 2, 3, 4]
        actual = sortStack(input)
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