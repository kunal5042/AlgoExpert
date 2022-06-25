class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_closest(tree, target, closest):
	if tree is None:
		return closest
	
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	
	if target > tree.value:
		return find_closest(tree.right, target, closest)
	elif target < tree.value:
		return find_closest(tree.left, target, closest)
	else:
		return target

def findClosestValueInBst(tree, target):
	inf = float("inf")
	return find_closest(tree, target, inf)

# Kunal Wadhwa
