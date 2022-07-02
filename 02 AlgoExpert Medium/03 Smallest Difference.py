# https://www.algoexpert.io/questions/smallest-difference
# Arrays

def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	result, smallest_difference = [None, None], float('inf')
	# idx1 corresponds to position in arrayOne and idx for arrayTwo
	idx1, idx2 = 0, 0
	while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
		ele1, ele2 = arrayOne[idx1], arrayTwo[idx2]
		# absolute difference
		difference = max(ele1, ele2) - min(ele1, ele2)
		# update the min difference found so far
		smallest_difference = min(difference, smallest_difference)
		if smallest_difference == difference:
			# if current difference is minimum, update the result
			result = [ele1, ele2]
		# in attempt to decrease the difference even further
		# we have to try bringing the ele1 and ele2 as close to each other as possible
		# that can only be done if we move ahead in the smaller element's direction
		# hence the increment
		if ele1 > ele2:
			idx2 += 1
			continue
		idx1 += 1

	return result


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
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