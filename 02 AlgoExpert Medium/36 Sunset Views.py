# https://www.algoexpert.io/questions/sunset-views
# Stacks

def sunsetViews(buildings, direction):
    return sunset_views(buildings, direction)

def sunset_views(buildings, direction):
	flag = True if direction == 'EAST' else False
	result = []
	
	if flag:
		stack = []
		max_height = float('-inf')
		for idx in reversed(range(len(buildings))):
			if buildings[idx] > max_height:
				stack.append(idx)
				max_height = buildings[idx]
		
		while len(stack) != 0:
			result.append(stack.pop())
	else:
		stack = []
		max_height = float('-inf')
		for idx in range(len(buildings)):
			if buildings[idx] > max_height:
				stack.append(idx)
				max_height = buildings[idx]
				
		result = stack
	
	return result

    


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''