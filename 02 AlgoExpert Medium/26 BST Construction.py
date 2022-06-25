#!/usr/bin/python
# -*- coding: utf-8 -*-
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        # if you don't want duplicate values uncomment the lines below, by default duplicate values will be inserted towards the left
        # if value == self.value:
            # return self

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
                if current.left is not None and current.right \
                        is not None:
                    current.value = current.right.get_min()
                    current.right.remove(current.value, current)
                    
                elif parent is None:
                    # edge case where we are asked to remove the root
                    # because there is only one node either in the left or the right

                    # so if there is a node in the left
                    # make this left node the new root
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left

                    elif current.right is not None:
                        # otherwise if there is a node in the right
                        # make this the new root

                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right

                    else:
                        # in this case, we are asked to delete the BST
                        # I'm not gonna delete, lol
                        # if you want, it's pretty simple

                        pass
                elif parent.left == current:

                    # depends on how you want to implement this, if you want to delete the binary tree
                    # uncomment the line below
                    # ....current.value = None

                    # we found the value to remove, and if the current node is a left node
                    # replace current node with it's left or right accordingly

                    parent.left = (current.left if current.left
                                    is not None else current.right)
                elif parent.right == current:

                    # if current node is a right node
                    # again replace the current node with it's left or right as per the condition of not being None

                    parent.right = (current.left if current.left
                                    is not None else current.right)
                break
        return self


root = BST(10)
root.insert(10)
root.insert(5)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(15)
root.insert(13)
root.insert(22)
root.insert(14)
root.insert(18)
root.insert(25)
root.insert(19)
root.remove(15)












# Kunal Wadhwa

