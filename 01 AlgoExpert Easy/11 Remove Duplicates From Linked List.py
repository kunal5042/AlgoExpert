# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
# Linked Lists

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
	
def removeDuplicatesFromLinkedList(linkedList):
	node = linkedList
	potential = None
	if node is None:
		return None
	else:
		potential = node
		while node.next is not None:
			node = node.next
			if potential.value == node.value:
				continue
			else:
				potential.next = node
				potential = node
	
	potential.next = None
	
	return linkedList



import unittest
class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())
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