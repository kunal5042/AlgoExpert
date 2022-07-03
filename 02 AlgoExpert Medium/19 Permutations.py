# https://www.algoexpert.io/questions/permutations
# Recursion

'''
O(n*n!) Time | O(n*n!) Space
'''
def getPermutations(array):
    # Write your code here.
	permutations = []
	helper(array, [], permutations)
	return permutations

def helper(array, cur_perm, perms):
	# if there are no elements from array to append and create a new perm
	# and cur_perm is not empty
	if len(array) == 0 and len(cur_perm) != 0:
		perms.append(cur_perm)
		
	else:
		for pop_index in range(len(array)):
			# remove the element at the pop_index 
			# create a new perm with that element 
			# send the remaining array and new permutation to helper
			# to do  this recursively 
			# until the array is empty and the permutation is complete 
			remaining_array = array[:pop_index] + array[pop_index + 1:]
			new_perm = cur_perm + [array[pop_index]]
			
			helper(remaining_array, new_perm, perms)
			


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)
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