import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(5)
        root.left = BST(2)
        root.right = BST(7)
        root.left.left = BST(1)
        root.left.right = BST(4)
        root.right.left = BST(6)
        root.right.right = BST(8)
        root.left.left.left = BST(0)
        root.left.right.left = BST(3)

        nodeOne = root
        nodeTwo = root.left
        nodeThree = root.left.right.left
        expected = True
        actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")
        
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    def is_descendant(node1, node2):
        if node2 is None:
            return False

        # simple check to see if node1 is a descendant of node2
        if node2.left == node1 or node2.right == node1:
            return True

        return is_descendant(node1, node2.left) or is_descendant(node1, node2.right)

    # if one is descendant and three is ancestor 
    if is_descendant(nodeOne, nodeTwo) is True:
        if is_descendant(nodeTwo, nodeThree) is True:
            return True

    # if three is descendant and one is ancestor 
    if is_descendant(nodeThree, nodeTwo) is True:
        if is_descendant(nodeTwo, nodeOne) is True:
            return True

    return False

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa