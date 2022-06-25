import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
        print("Test Case: Passed")
        
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    '''
    O(v + e) Time: where v is the number of vertices in the graph and e is the number of edges 
    '''
    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)

        return array
    
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

''' Kunal Wadhwa ''' 
