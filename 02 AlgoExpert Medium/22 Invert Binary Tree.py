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

# Kunal Wadhwa
