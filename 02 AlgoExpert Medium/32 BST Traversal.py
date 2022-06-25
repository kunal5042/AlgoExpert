import unittest
from colorama import Fore


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def inOrderTraverse(tree, array):
	inorder(tree, array)
	return array

def preOrderTraverse(tree, array):
	pre_order(tree, array)
	return array

def postOrderTraverse(tree, array):
	post_order(tree, array)
	return array

def inorder(tree, array):
	if tree is None:
		return
	inorder(tree.left, array)
	array.append(tree.value)
	inorder(tree.right, array)

def pre_order(tree, array):
	if tree is None:
		return
	array.append(tree.value)
	pre_order(tree.left, array)
	pre_order(tree.right, array)

def post_order(tree, array):
	if tree is None:
		return
	post_order(tree.left, array)
	post_order(tree.right, array)
	array.append(tree.value)
	

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]
        
        try:
            self.assertEqual(inOrderTraverse(root, []), inOrder)
            self.assertEqual(preOrderTraverse(root, []), preOrder)
            self.assertEqual(postOrderTraverse(root, []), postOrder)
            print(Fore.GREEN + f'\nTest Case: Passed\n')
        except:
            print(Fore.RED + f'\nTest Case: Failed\n')


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
