import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

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
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)
        print("Test Case: Passed")

def mergeLinkedLists(headOne, headTwo):
    iter1 = headOne
    prev_iter1 = None
    iter2 = headTwo

    while iter1 is not None and iter2 is not None:
        if iter1.value < iter2.value:
            prev_iter1 = iter1
            iter1 = iter1.next
        else:
            if prev_iter1 is not None:
                prev_iter1.next = iter2

            prev_iter1 = iter2
            iter2 = iter2.next
            prev_iter1.next = iter1

        if iter1 is None:
            prev_iter1.next = iter2


    return headOne if headOne.value < headTwo.value else headTwo

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa