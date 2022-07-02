# https://www.algoexpert.io/questions/find-closest-value-in-bst
# Binary Search Trees

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



import unittest
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa
# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''