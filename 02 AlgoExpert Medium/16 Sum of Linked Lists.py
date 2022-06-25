# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    return sum_of_linked_list(linkedListOne, linkedListTwo)

'''
O(max(n, m)) Time | O(max(n, m)) Space: where n is the length of the first linked list and,
m is the length of the second linked list
'''
def sum_of_linked_list(list1, list2):
	# safe check
	if list1 is not None and list2 is not None:
		# creating the resultant list with the garbage value
		result_head = LinkedList(0)
		# storing it's reference for later use in operations
		current = result_head
		# if sum of node1.value + node2.value > 10, there will be a carry 
		carry = 0
		# references
		node_one = list1
		node_two = list2
		# while either of the lists are not fully traversed
		while node_one is not None or node_two is not None or carry != 0:
			value_one = 0
			if node_one is not None:
				value_one = node_one.value
				
			value_two = 0
			if node_two is not None:
				value_two = node_two.value
			# resultant sum
			sum_values = value_one + value_two + carry
			# we can add only one digit and it can't be equal or greater than 10, hence modulo 10
			resultant_value = sum_values % 10
			# update the result
			current.next = LinkedList(resultant_value)
			# to store the next value
			current = current.next
			# if the sum was greater than 10, we have a carry equal to sum // 10
			carry = sum_values // 10
			# in our while we check if either of the two lists are not None, keep looping
			# so, when one of the two lists points to None, we can't just
			# set None = None.next, hence we are checking if it's not None
			# before moving ahead
			node_one = node_one.next if node_one is not None else None
			node_two = node_two.next if node_two is not None else None
		# discard the garbage value and return the resultant list from head.next onwards
		return result_head.next
	else:
		# one of the lists is None
		# hence return the list which is not empty, coz that's our resultant list
		if list1 is not None:
			return list2
		else:
			return list1