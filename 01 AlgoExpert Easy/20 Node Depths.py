# https://www.algoexpert.io/questions/node-depths
# Binary Trees

'''Recursive approach'''
def nodeDepths(root, depth=0):
	if root is None: return 0
	
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
	#return node_depths_iterative(root)

'''Iterative approach'''
def node_depths_iterative(root):
	sum_dep = 0
	stack = [{'node': root, 'depth': 0}]
	while len(stack):
		node_info = stack.pop()
		node, depth = node_info['node'], node_info['depth']
		if node is None: continue
		
		sum_dep += depth
		stack.append({'node': node.left, 'depth': depth+1})
		stack.append({'node': node.right, 'depth': depth+1})
	return sum_dep;
	
	
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Kunal Wadhwa
