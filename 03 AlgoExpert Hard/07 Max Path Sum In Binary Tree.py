import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(maxPathSum(test), 18)
        print("Test Case: Passed")


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


def maxPathSum(tree):
    # Write your code here.
    _, max_sum = find_max_sum(tree)
    return max_sum

def find_max_sum(tree):
    if tree is None:
        return (float('-inf'), float('-inf'))

    # LMSB = Left Max Sum as Branch
    # LMPS = Left Max Path Sum
    LMSB, LMPS = find_max_sum(tree.left)
    RMSB, RMPS = find_max_sum(tree.right)

    # MCSB = Max Child Sum as Branch
    MCSB   = max(LMSB, RMSB)

    value  = tree.value
    # MSB  = Max Sum as Branch for current node
    MSB    = max(MCSB+value, value)
    # MSRN = Max Sum as Root Node
    MSRN   = max(LMSB + value + RMSB, MSB)
    # MPS  = Max Path Sum
    MPS    = max(LMPS, RMPS, MSRN)

    return (MSB, MPS)


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
