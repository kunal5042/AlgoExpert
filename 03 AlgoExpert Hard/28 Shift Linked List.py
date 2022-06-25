class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


'''
O(n) Time and O(1) Space: where n is the number of nodes in the linked list
'''
def shiftLinkedList(head, k):
    len_list = 1
    tail = head

    while tail.next is not None:
        tail = tail.next
        len_list += 1


    offset = abs(k) % len_list
    if offset == 0: return head

    move_ahead = len_list - offset if k > 0 else offset
    current = head
    for _ in range(1, move_ahead):
        current = current.next

    new_head = current.next
    # tail
    current.next = None
    tail.next = head

    return new_head


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
