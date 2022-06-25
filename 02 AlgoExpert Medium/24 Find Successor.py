# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

'''Solution 1: Naive'''
def findSuccessor(tree, node):
	traversal = inorder(tree)
	for idx in range(len(traversal)):
		if traversal[idx] is node and idx != len(traversal)-1:
			return traversal[idx+1]
		if idx == len(traversal)-1:
			return None
	
def inorder(tree):
	result = []
	def F(root, result):
		if root is not None:
			F(root.left, result)
			result.append(root)
			F(root.right, result)
	F(tree, result)
	return result

'''Solution 2: Efficient'''
def findSuccessorEff(tree, node):
	if node.right is not None:
		return left_most_child(node.right)
	return right_most_parent(node)

def left_most_child(node):
	curr = node
	while curr.left is not None:
		curr = curr.left
	return curr

def right_most_parent(node):
	curr = node
	while curr.parent is not None and curr.parent.right == curr:
		curr = curr.parent
	return curr.parent

# Kunal Wadhwa
