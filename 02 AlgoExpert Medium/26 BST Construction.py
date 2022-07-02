# https://www.algoexpert.io/questions/bst-construction
# Binary Search Trees

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		#if you don't want duplicate values uncomment the lines below, by default duplicate values will be inserted towards the left
		#if value == self.value:
		#	return self
		
		# remaining lines need no explanation but.
		# if value is greater, move towards right subtree to find where to insert the value
		# if value is smaller, move towards left subree 
		# insert when you reach bottom 
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
				return self
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
				return self
			else:
				self.right.insert(value)
				
	def contains(self, value):
		# similar as insert
		# eliminate half of the tree at each step and keep looking for the value
		# return boolean accordingly 
		if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True			
	
	def get_min(self):
		c_node = self
		while c_node.left is not None:
			c_node = c_node.left
		# min node will be a leaf, so we can return just the node.value
		return c_node.value
	
	def remove(self, value, parent=None):
		current = self
		while current is not None:
			# find the value 
			if value < current.value:
				parent = current
				# move towards left
				current = current.left
				
			elif value > current.value:
				parent = current
				# move towards right
				current = current.right
				
			else:
				# found the value to remove
				
				# if both it's subtrees are not None
				# find the min value in the right subtree
				# make it current node's value
				# remove the value from the right subtree
				if current.left is not None and current.right is not None:
					current.value = current.right.get_min()
					current.right.remove(current.value, current)
					
				# edge case where we are asked to remove the root
				elif parent is None:
					# because there is only one node either in the left or the right
					
					# so if there is a node in the left
					# make this left node the new root
					if current.left is not None:
						current.value = current.left.value
						current.right = current.left.right
						current.left = current.left.left
						
					# otherwise if there is a node in the right
					# make this the new root
					elif current.right is not None:
						current.value = current.right.value
						current.left = current.right.left
						current.right = current.right.right
					
					# in this case, we are asked to delete the BST
					# I'm not gonna delete, lol
					# if you want, it's pretty simple 
					else:
						pass
					# depends on how you want to implement this, if you want to delete the binary tree
					# uncomment the line below
					#	current.value = None
				
				# we found the value to remove, and if the current node is a left node
				# replace current node with it's left or right accordingly 
				elif parent.left == current:
					parent.left = current.left if current.left is not None else current.right
				# if current node is a right node
				# again replace the current node with it's left or right as per the condition of not being None
				elif parent.right == current:
					parent.right = current.left if current.left is not None else current.right
				break
		return self




import unittest
BST = BST


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))
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