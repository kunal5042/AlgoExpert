'''
O(n) Time | O(1) Space: where n is the number of nodes in the list
'''
def removeKthNodeFromEnd(head, k):
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next


import unittest
class LinkedListClass:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(LinkedListClass):
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
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa