# https://www.algoexpert.io/questions/single-cycle-check
# Graphs

'''
LOGIC:
We are checking below two conditions to determine if we have a single cycle or not.
    1. We are not getting back at the STARTING_IDX before visiting len(array) elements
    2. After visiting len(array) elements if we are back at STARTING_IDX or not
'''
def hasSingleCycle(array):
    visited_count = 0
    
    STARTING_IDX  = 0
    # You can start with any index
    current_idx   = 0
    
    # so long that we haven't visited len(array) elements
    while visited_count < len(array):
        # if more than one element has been visited, and yet we are back at the starting index
        if visited_count > 0 and current_idx == STARTING_IDX:
            return False

        visited_count += 1
        current_idx   += array[current_idx]
        current_idx   %= len(array)

    # we have visited n elements, now if we are back at the starting idx 
    # we have single cycle, else not
    return True if current_idx == STARTING_IDX else False




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hasSingleCycle([2, 3, 1, -4, -4, 2]), True)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''