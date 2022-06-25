# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	result = []
	return helper(root, 0, result)

def helper(node, run_sum, result):
	if node is None: return
	if node.left is None and node.right is None:
		result.append(run_sum + node.value)
	
	helper(node.left, run_sum+node.value, result)
	helper(node.right, run_sum+node.value, result)
	
	return result

# Kunal Wadhwa
