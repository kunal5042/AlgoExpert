# https://www.algoexpert.io/questions/three-number-sum
# Arrays

'''
O(n**2) Time and O(n) Space
'''
def threeNumberSum (array, targetSum):
    list = []

    # so that we can use the two-pointer approach
    array.sort(reverse = False)

    for index in range(len(array)-2):
        # using the two pointers
        first, last = index + 1, len(array)-1

        # they can't be equal because we need unique elements
        while first < last:
            # this is our potential possible triplet
            potential = array[first] + array[last] + array[index]
            
            if(potential == targetSum):
                tempList = [array[index], array[first], array[last]]

                # we can directly append and we don't need to sort
                # because of the approach and the fashion in which we are inserting
                # it's already going to be sorted
                list.append(tempList)

                # keep looking for more
                last += -1
                first += 1

            elif(potential > targetSum):
                last  -= 1
            
            elif(potential < targetSum):
                first += 1
    
    return list


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
        print("Test Case: Passed")
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

'''

Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''