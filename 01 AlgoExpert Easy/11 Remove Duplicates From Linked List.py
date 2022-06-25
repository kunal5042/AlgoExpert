# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

'''
O(n) Time | O(1) Space: where n is the number of nodes in the linked list
'''
def removeDuplicatesFromLinkedList(linkedList):
	current = linkedList
	while current is not None:
		next_distinct_node = current.next
		
		# if following nodes are duplicate, move ahead till a non duplicate node is found or till the end 
		# if all nodes are duplicate
		while next_distinct_node is not None and next_distinct_node.value == current.value:
			next_distinct_node = next_distinct_node.next
			
		# remove duplicates by pointing current node's next to the non duplicate node
		# the line below won't affect current's next value if the above while loop doesn't run even once
		current.next = next_distinct_node
		# move ahead by moving current to current's next
		current = current.next
		
	return linkedList

# Kunal Wadhwa
