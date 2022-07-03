# https://www.algoexpert.io/questions/validate-bst
# Binary Search Trees

def validate_bst(root, lower_bound=float('-inf'), upper_bound=float('inf')):
	if root is None:
		return True
	
	if root.value >= upper_bound or root.value < lower_bound:
		return False
		
	left_is_binary = validate_bst(root.left, lower_bound, root.value)
	right_is_binary = validate_bst(root.right, root.value, upper_bound)
	
	return left_is_binary and right_is_binary
	
def validateBst(tree):
	return validate_bst(tree)



import unittest
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        self.assertEqual(validateBst(root), True)
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