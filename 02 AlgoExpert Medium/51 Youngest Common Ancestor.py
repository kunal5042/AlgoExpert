# https://www.algoexpert.io/questions/youngest-common-ancestor
# Graphs

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

"""O(d) Time and O(d) Space: where d is the depth of the ancestor tree"""
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # keep track of visited nodes in a hash_map
    visited = {}

    # start with any of the descendants and traverse it's ancestors up the ladder till the topAncestor
    # and while traversing mark them visited
    current = descendantOne
    while current != topAncestor:
        visited[current] = True
        current          = current.ancestor

    # now take the other ancestor, and do the same
    # the first node that we find which is already visited is our youngest common ancestor
    # as that node has already been visited by the other descendant implies that this node is an ancestor to that
    # descendant too
    current = descendantTwo
    while current != topAncestor:
        if current in visited and visited[current] is True:
            return current
        visited[current] = True
        current = current.ancestor

    # if no common node is found
    # that implies that our youngest common ancestor is the topAncestor itself
    return topAncestor

"""O(d) Time and O(1) Space: where d is the depth of the ancestor tree"""
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    def getDescendantDepth(descendant, topAncestor):
         depth = 0
         while descendant != topAncestor:
             depth += 1
             descendant = descendant.ancestor
         return depth

    # get depth of both the descendants
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    # find the lower of the two descendants
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    # bring the lower descendant to the same level as the higher descendant
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    # once they are on the same level
    # back track until they are equal or until we reach a common ancestor
    # and that will be our youngest common ancestor
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant



import unittest
class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''