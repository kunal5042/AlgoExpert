# https://www.algoexpert.io/questions/merge-overlapping-intervals
# Arrays

'''
O(n(log(n))) Time and O(1) Extra Space: where n is the length of the input array 
'''
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = intervals[0]
    result = []
    
    for idx in range(1, len(intervals)):
        current = intervals[idx]
        
        if merged[1] < current[0]:
            # not overlapping
            result.append(merged)
            merged = current
            
        else:
            # overlapping
            merged[0] = min(merged[0], current[0])
            merged[1] = max(merged[1], current[1])
            
        # no need to merge further 
        if idx == len(intervals) - 1:
            result.append(merged)
            
    return result
'''
O(n(log(n))) Time and O(1) Extra Space: where n is the length of the input array 
'''
def merge_overlapping(intervals):
	# not allowed to mutate the given input
	array = intervals
	array.sort(key = lambda x: x[0])
	# array with merged overlapping intervals
	result = []
	
	idx = 0
	while idx < len(array):
		if idx == len(array) - 1:
			# can't compare with the next interval
			result.append(array[idx])
			break
		
		this_interval = array[idx]
		next_interval = array[idx+1]
		
		if this_interval[1] > next_interval[0] or this_interval[1] == next_interval[0]:
			# found overlapping
			
			start = idx
			end = idx + 1
			# this is gonna be our replacement interval's end time
			upper_bound = array[start][1]
			merge = []
			
			# So, while these intervals are overlapping
			while start < len(array) - 1 and upper_bound >= array[end][0]:
				lower_bound = array[idx][0]
				upper_bound = max(array[idx][1], array[end][1])
				# keep updating what the merged interval would look like, when loop ends
				merge = [lower_bound, upper_bound]
				start +=1
				end += 1
			
			# add the replacement/merged interval to the result
			result.append(merge)
			# coz, we have merged all the overlapping intervals before end, we can continue checking from the end
			idx = end
		else:
			# if they don't overlap, add the current interval to the result
			result.append(array[idx])
			idx += 1
	
	# return result
	return result



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals)
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