# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
	return is_height_balanced(tree)

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

# Kunal Wadhwa
