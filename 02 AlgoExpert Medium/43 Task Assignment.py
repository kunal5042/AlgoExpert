import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[4, 2], [0, 5], [3, 1]]
        actual = taskAssignment(k, tasks)
        self.assertEqual(actual, expected)
        print('Test Case: Passed')

def taskAssignment(k, tasks):
    result = []
    sorted_tasks = sorted(tasks)

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

        result.append([task1_index, task2_index])

    return result

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()

# Kunal Wadhwa  
