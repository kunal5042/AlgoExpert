class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

'''
O(n) Time and O(1) Space: where n is the number of nodes in the Linked List
'''
def findLoop(head):
    # Using Floyd's Cycle Detection Algorithm
    slow  = head
    fast  = head
    cycle = False

    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

        # if this list has a cycle, slow will become equal to fast
        if slow == fast:
            cycle = True
            break


    # point back slow to start
    if cycle is True:
        slow = head


    # move both pointers at the speed of the slow
    # to reach the start of the cycle
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Kunal Wadhwa
        