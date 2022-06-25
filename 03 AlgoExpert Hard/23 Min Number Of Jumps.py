# O(n^2) Time and O(n) Space: where n is the lenght of the array
def minNumberOfJumps(array):
    minjumps = [0 for _ in array]

    for idx in range(1, len(array)):
        for jdx in range(0, idx):
            if idx - jdx - array[jdx] <= 0:
                minjumps[idx] += minjumps[jdx] + 1
                break


    return minjumps[-1]
    
'''
The Idea:
Goal: To calculate the minimum number of jumps to reach from 0th index to last index.

The function should return the number of jumps.

How to minimize the number of jumps?
A: Follow the path with allows maximum number of steps, thereby minimizing the number of jumps required.

How to find such path?
But, even before that, when do we need to make another jump?
A: When all the available steps are used.

Can we use the information above to find out when we need to make a jump?
A: Yes, as soon as the steps are exhausted, make another jump.

But, how to minimize those jumps?
A: We need to make a smart jump.
And, the smartest jump would be from the element/index in the array which allows the maximum number of steps.

Hear me out!
Instead of finding the smartest jump, if we we can find the number of available steps we would have if we had made that jump.
That would allow us to find when to make the next jump.
As, we only need to know the available number of steps in order to find the number of jumps.

With that information, Read the code.
'''
# O(n) Time and O(1) Space
def minNumberOfJumps(array):
    if len(array) == 1: return 0
        
    jumps = 0
    available_steps = array[0]
    maximum_reach   = array[0] + 0 # element + it's index

    for idx in range(1, len(array)-1):
        # maximum reach will keep track of the maximum index we can reach of all the paths seen so far
        maximum_reach = max(maximum_reach, array[idx] + idx)

        # at every iteration, we are using up a step
        available_steps -= 1

        # we need to make that smart jump
        if available_steps == 0:
            # idx being the index where we have exhausted our available steps
            # hence, if we would have made the smartest jump
            # we would now these many steps
            available_steps = maximum_reach - idx

            # another jump 
            jumps += 1


    return jumps + 1



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)
        print("Test Case: Passed")


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa