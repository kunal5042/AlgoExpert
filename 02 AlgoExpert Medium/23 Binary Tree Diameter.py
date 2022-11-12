# https://www.algoexpert.io/questions/binary-tree-diameter
# Binary Trees

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

'''Recursive Solution 1'''
def binary_tree_diameter(root, diameter=0):
	if root is None: return diameter
	
	current_diameter = max_height(root.left) + max_height(root.right)
	return max(current_diameter, binary_tree_diameter(root.left), binary_tree_diameter(root.right))

def max_height(root, height=0):
	if root is None:
		return height
	
	height += 1
	return max(max_height(root.left, height), max_height(root.right, height))

'''Recursive Solution 2'''
def binaryTreeDiameter(root):
    return get_tree_info(root).diam

def get_tree_info(root):
	if root is None: return TreeInfo(0, 0)

	left_tree_info = get_tree_info(root.left)
	right_tree_info = get_tree_info(root.right)
	
	longest_path_through_root = left_tree_info.height + right_tree_info.height
	max_diam = max(left_tree_info.diam, right_tree_info.diam)
	cur_diam = max(longest_path_through_root, max_diam)
	cur_height = 1 + max(left_tree_info.height, right_tree_info.height)
	
	return TreeInfo(cur_diam, cur_height)
	
class TreeInfo:
	def __init__(self, diam, height):
		self.diam = diam
		self.height = height



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''