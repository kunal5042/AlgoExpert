import unittest
from colorama import Fore

def minHeightBst(array):
    return create(array, None, 0, len(array)-1)

def create(array, root, start, end):
	if end < start:
		return
	
	middle = (start+end) // 2
	
	if root is not None:
		root.insert( array[middle] )
	else:
		root = BST( array[middle] )
	
	create(array, root, start, middle-1)
	create(array, root, middle+1, end)
	
	return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
				
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBst(array)
        
        try:
            self.assertTrue(validateBst(tree))
            self.assertEqual(getTreeHeight(tree), 4)

            inOrder = inOrderTraverse(tree, [])

            self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])

            print(Fore.GREEN + f'\nTest Case: Passed\n')
        except:
            print(Fore.RED + f'\nTest Case: Failed\n')


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
