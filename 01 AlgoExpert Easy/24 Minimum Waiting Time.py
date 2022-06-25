import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = minimumWaitingTime(queries)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")
        

def minimumWaitingTime(queries):
	current_wt = 0
	total_waiting_time = 0
	queries.sort()
	
	for idx in range(1, len(queries)):
		current_wt += queries[idx-1]
		total_waiting_time += current_wt
		
	return total_waiting_time

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
