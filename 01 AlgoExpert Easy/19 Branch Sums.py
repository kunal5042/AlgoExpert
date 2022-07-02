# https://www.algoexpert.io/questions/branch-sums
# Binary Trees

'''O(n) Time and O(n) Space'''
def branchSums(root):
    def BS(root, rsum=0, result=[]):
        if root is None:
            return 
            
        if root.left is None and root.right is None:
            result.append(rsum+root.value)

        BS(root.left, rsum+root.value, result)
        BS(root.right, rsum+root.value, result)
        return result
        
    return BS(root)




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])
        print("Test Case: Passed")

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

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