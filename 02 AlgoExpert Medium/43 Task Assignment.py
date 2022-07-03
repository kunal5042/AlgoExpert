# https://www.algoexpert.io/questions/task-assignment
# Greedy Algorithms

'''Solution - 1'''
# O(nlog(n)) time | O(n) space - where n is the number of tasks
def taskAssignment(k, tasks):
    result = []
    # create a sorted list from the input list
    sorted_tasks = sorted(tasks)

    # map the indices of the elements in the list to their value
    # {key, value} = {element, list of indices in the unsorted list [idx1, idx2]}
    # we store list of indices because there might be duplicate elements
    def map_duration_to_indices():
        mapped_indices = {}

        for idx, duration in enumerate(tasks):
            if duration in mapped_indices:
                mapped_indices[duration].append(idx)
            else:
                mapped_indices[duration] = [idx]
        return mapped_indices


    mapped_indices = map_duration_to_indices()
    for idx in range(k):
        task1 = sorted_tasks[idx]
        list_of_indices = mapped_indices[task1]
        task1_index = list_of_indices.pop()
        
        task2 = sorted_tasks[len(tasks)-1-idx]
        list_of_indices = mapped_indices[task2]
        task2_index = list_of_indices.pop()

        # pair the largest duration task with the corresponding smallest duration task
        # for optimal allocation
        result.append([task1_index, task2_index])

    return result

'''Solution - 2'''
'''Same Idea'''
# O(nlog(n)) time | O(n) space - where n is the number of tasks
def taskAssignment(k, tasks):
    if k == 1:
        return [[x for x in range(len(tasks))]]

    visited = [False for task in tasks]
    result  = [[] for worker in range(k)]

    def get_greatest():
        greatest     = 0
        greatest_idx = None
        for idx, task in enumerate(tasks):
            if task > greatest and visited[idx] is False:
                greatest     = task
                greatest_idx = idx

        visited[greatest_idx] = True
        return greatest_idx
        
    for idx in range(len(result)):
        result[idx].append(get_greatest())

    for idx in reversed(range(len(result))):
        result[idx].append(get_greatest())

    return result




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[4, 2], [0, 5], [3, 1]]
        actual = taskAssignment(k, tasks)
        for task in actual  : task.sort()
        for task in expected: task.sort()
        self.assertEqual(sorted(actual), sorted(expected))

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