# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst
# Binary Search Trees

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, number_of_nodes_visited, latest_visited_node_value):
        self.visited_count = number_of_nodes_visited
        self.latest_value  = latest_visited_node_value

def findKthLargestValueInBst(tree, k):
    def reverse_inorder(root, k, tree_info):
        if root is None:
            return

        reverse_inorder(root.right, k, tree_info)
        if tree_info.visited_count < k:
            tree_info.visited_count += 1
            tree_info.latest_value   = root.value
            reverse_inorder(root.left, k, tree_info)

    tree_info = TreeInfo(0, -1)
    reverse_inorder(tree, k, tree_info)
    return tree_info.latest_value



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''