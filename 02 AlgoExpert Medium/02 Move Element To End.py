# https://www.algoexpert.io/questions/move-element-to-end
# Arrays

def moveElementToEnd(array, toMove):
	return move_to_end(array, toMove)

def move_to_end(array, to_move):
	# Algorithm
	# Move all the elements which are not equal to toMove to the front
	# By the end of the traversal all the toMove elements will be at the end 
	# front index = to_put_at
	to_put_at = 0
	for idx in range(len(array)):
		if array[idx] != to_move:
			# if current is not equal to target
			# move current to the front
			array[idx], array[to_put_at] = array[to_put_at], array[idx]
			# new front 
			to_put_at +=1
	return array



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)
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