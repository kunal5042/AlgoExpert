# https://www.algoexpert.io/questions/invert-binary-tree
# Binary Trees

def invertBinaryTree(tree):
	root = tree
	invert_binary_tree(root)
	return root
	
'''Recursive: O(n) Time and O(d): n - number of nodes, d - depth'''
def invert_binary_tree(root):
	if root is not None:
		root.left, root.right = root.right, root.left
		
		invert_binary_tree(root.left)
		invert_binary_tree(root.right)
		
'''Iterative: O(n) Time and O(n)'''
def invert_binary_tree_iterative(root):
	q = [root]
	while len(q):
		node = q.pop(0)
		if node is None: continue
		node.left, node.right = node.right, node.left
		q.append(node.left)
		q.append(node.right)
		

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



import unittest
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
        invertBinaryTree(tree)
        self.assertTrue(tree.__eq__(invertedTree))
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''