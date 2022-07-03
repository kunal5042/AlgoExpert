# https://www.algoexpert.io/questions/height-balanced-binary-tree
# Binary Trees

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, is_balanced, height):
        self.balanced = is_balanced
        self.height   = height

def heightBalancedBinaryTree(tree):
    def get_tree_info(node):
        if node is None:
            return TreeInfo(True, -1)

        left_subtree  = get_tree_info(node.left)
        right_subtree = get_tree_info(node.right)

        current_balanced = (
            left_subtree.balanced \
            and right_subtree.balanced \
            and abs(left_subtree.height - right_subtree.height) <= 1 \
        )

        current_height  = max(left_subtree.height, right_subtree.height) + 1

        return TreeInfo(current_balanced, current_height)

    # call the helper to get the tree info for the root
    return get_tree_info(tree).balanced
    

def is_height_balanced(root):
	if root is None:
		return True
	# if difference between heights > 1: RETURN FALSE
	difference = abs(get_height(root.left) - get_height(root.right))
	if difference > 1:
		return False
	# Check this for every node
	return is_height_balanced(root.left) and is_height_balanced(root.right)
	
def get_height(root, height=0):
	if root is None:
		return height
	
	height += 1
	return max(get_height(root.left, height), get_height(root.right, height))




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        expected = True
        actual = heightBalancedBinaryTree(root)
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