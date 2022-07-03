# https://www.algoexpert.io/questions/breadth-first-search
# Graphs

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    '''O(v+e) Time and O(v) Space'''
    def breadthFirstSearch(self, array):
        q = [self]

        while len(q) > 0:
            # This count variable let's us keep track of levels if we want to [Optional]
            count = len(q)
            for _ in range(count):
                # pop all the nodes from the graph
                node = q.pop(0)
                # append their names to the resultant array
                array.append(node.name)
                # enqueue all their children to the queue
                for child in node.children:
                    q.append(child)

                # keep repeating these steps, until there is a node in the queue

        # return the result
        return array



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

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