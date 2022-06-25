import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.right.right.left = BinaryTree(7)
        root.right.right.right = BinaryTree(8)
        target = 3
        k = 2
        expected = [2, 7, 8]
        actual = findNodesDistanceK(root, target, k)
        actual.sort()
        self.assertCountEqual(actual, expected)
        print("Test Case: Passed")

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    parents = {}
    seen    = {}
    result  = []

    def get_parents(node, node_parent):
        if node is None:
            return
        parents[node] = node_parent
        seen[node]    = False
        get_parents(node.left, node)
        get_parents(node.right, node)

    def get_target():
        for node, parent in parents.items():
            if node.value == target:
                return node

    def expand_from_target():
        get_parents(tree, None)
        target_node = get_target()
        
        queue = [(target_node, 0)]
        while len(queue):
            count = len(queue)
            for _ in range(count):
                node_tuple = queue.pop(0)
                cnode = node_tuple[0]
                cdist = node_tuple[1]
                seen[cnode] = True
                if cdist == k:
                    result.append(cnode.value)

                if cnode.left is not None and seen[cnode.left] is False:
                    queue.append((cnode.left, cdist+1))

                if cnode.right is not None and seen[cnode.right] is False:
                    queue.append((cnode.right, cdist+1))

                if parents[cnode] is not None and seen[parents[cnode]] is False:
                    queue.append((parents[cnode], cdist+1))

    expand_from_target()
    return result


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa

