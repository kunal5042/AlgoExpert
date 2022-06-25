import unittest
from colorama import Fore

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return is_valid(tree.left, float('-inf'), tree.value) and is_valid(tree.right, tree.value, float('inf'))


def is_valid(node, lower, upper):
    if node is None:
        return True
    
    if node.value < lower or node.value >= upper:
        return False
    
    return is_valid(node.left, lower, node.value) and is_valid(node.right, node.value, upper)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        try:
            self.assertEqual(validateBst(root), True)
            print(Fore.GREEN + f'\nTest Case: Passed\n')
        except:
            print(Fore.RED + f'\nTest Case: Failed\n')


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
    
# Kunal Wadhwa

	
	
	