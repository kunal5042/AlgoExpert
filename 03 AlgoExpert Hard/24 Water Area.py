# O(n) Time and Space: where n is the length of the input array
def waterArea(heights):
    maxes = [0 for x in heights]
    left_max = 0
    for idx in range(len(heights)):
        height = heights[idx]
        maxes[idx] = left_max
        left_max = max(left_max, height)

    right_max = 0
    for idx in reversed(range(len(heights))):
        height = heights[idx]
        min_height =  min(right_max, maxes[idx])
        if height < min_height:
            maxes[idx] = min_height - height
        else:
            maxes[idx] = 0
        right_max = max(right_max, height)

    return sum(maxes)

# O(n) Time and O(1) Space
def water_area(heights):
    if len(heights) == 0:
        return 0

    left, right = 0, len(heights)-1
    max_left, max_right = heights[left], heights[right]
    water_collected = 0
    
    while left < right:
        if heights[left] < heights[right]:
            left += 1
            max_left = max(heights[left], max_left)
            water_collected += max_left - heights[left]

        else:
            right -= 1
            max_right = max(heights[right], max_right)
            water_collected += max_right - heights[right]

    return water_collected
    


'''
Try to find the water above at every index.
Things to consider
    - Is there a pillar on the index we are calculating for

For any given index in our array, whether it's a pillar or not.
We need to find two things
    - What's the tallest pillar to it's left
    - What's the tallest pillar to it's right

Using this information, we can find the water collected
'''

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48)
        print("Test Case: Passed")
        
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
