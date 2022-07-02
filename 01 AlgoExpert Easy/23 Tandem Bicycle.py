# https://www.algoexpert.io/questions/tandem-bicycle
# Greedy Algorithms

def tandem_bicycle(red, blue, fastest):
	if fastest is True:
		red.sort(reverse=True)
		blue.sort()
		result = 0
		for idx in range(len(red)):
			result += max(red[idx], blue[idx])
		return result
	else:
		red.sort()
		blue.sort()
		result = 0
		for idx in range(len(red)):
			result += max(red[idx], blue[idx])
		return result

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    red = redShirtSpeeds
    blue = blueShirtSpeeds
    return tandem_bicycle(red, blue, fastest)



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)
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