# https://www.algoexpert.io/questions/minimum-waiting-time
# Greedy Algorithms

'''O(n log(n)) Time and O(1) Space'''
def minimumWaitingTime(queries):
	current_wt = 0
	total_waiting_time = 0
	queries.sort()
	
	for idx in range(1, len(queries)):
		current_wt += queries[idx-1]
		total_waiting_time += current_wt
		
	return total_waiting_time



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = minimumWaitingTime(queries)
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