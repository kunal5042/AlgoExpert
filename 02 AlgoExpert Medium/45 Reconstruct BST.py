# https://www.algoexpert.io/questions/reconstruct-bst
# Binary Search Trees

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# we need this class, because we need a global value
class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx

def reconstructBst(preOrderTraversalValues):
    # start with idx = 0
    tree_info = TreeInfo(0)
    return reconstruct_bst_from_range(float('-inf'), float('inf'), preOrderTraversalValues, tree_info)

def reconstruct_bst_from_range(lower_bound, upper_bound, preOrderTraversalValues, current_subtree_info):
    # First base case
    # we have finished creating the entire tree
    if current_subtree_info.root_idx == len(preOrderTraversalValues):
        return None

    root_value = preOrderTraversalValues[current_subtree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        # not a valid node to be added
        return None

    # current root_value is valid, so create a BST node out of it
    # but first calculate it's left and right subtree's node
    current_subtree_info.root_idx += 1
    left_subtree = reconstruct_bst_from_range(lower_bound, root_value, preOrderTraversalValues, current_subtree_info)
    right_subtree = reconstruct_bst_from_range(root_value, upper_bound, preOrderTraversalValues, current_subtree_info)
    
    return BST(root_value, left_subtree, right_subtree)



import unittest
BST = BST


def getDfsOrder(node, values):
    if node is None:
        return
    values.append(node.value)
    getDfsOrder(node.left, values)
    getDfsOrder(node.right, values)
    return values


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
        tree = BST(10)
        tree.left = BST(4)
        tree.left.left = BST(2)
        tree.left.left.left = BST(1)
        tree.left.right = BST(3)
        tree.right = BST(17)
        tree.right.right = BST(19)
        tree.right.right.left = BST(18)
        expected = getDfsOrder(tree, [])
        actual = reconstructBst(preOrderTraversalValues)
        actualDfsOrder = getDfsOrder(actual, [])
        self.assertEqual(actualDfsOrder, expected)
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