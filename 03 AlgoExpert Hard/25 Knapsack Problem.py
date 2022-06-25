'''
O(nc) Time and Space: where n is the number of items and c is the capacity of the knapsack
'''
def knapsackProblem(items, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]

    for idx in range(1, len(items)+1):
        val, weight = items[idx-1]

        for jdx in range(1, capacity+1):
            # if knapsacks's current capacity is greater than weight, we can add more than just one item
            if jdx >= weight:
                
                # since, every idx,jdx cell in dp stores the maximum value that we can make with that capacity
                # we can use the remaining weight, that is knapsack's current capacity - weight of this item
                # very effeciently, by using the dp[current capacity - current weight]
                
                dp[idx][jdx] = max(dp[idx-1][jdx-weight] + val, dp[idx-1][jdx])
            
            else:

                # otherwise, since current weight is more than knapsack's current capacity
                dp[idx][jdx] = dp[idx-1][jdx]

    idx = 1
    flag = True
    for row in dp:
        if flag:
            flag = not flag
            continue
        print(items[idx-1], row)
        idx+=1

    # building sequence using backtracking
    sequence = []
    idx = len(dp)-1
    jdx = len(dp[0])-1

    while idx > 0:
        # as long as the current cell's value is same as the previous row's same cell's value
        # keep moving to previous row, while row > 0
        if dp[idx][jdx] == dp[idx-1][jdx]:
            idx -= 1
            
        else:
            # if current cell's value is different than previous's row's same cell's value
            # that implies we used this item to change this value
            # append it's index
            sequence.append(idx-1)

            # we decide the next cell to move to by finding which previous cell might have been used to calculate this value
            # we do that by subtracting current column/current capacity by the weight of the item we found
            jdx -= items[idx-1][1]

            # then we move to previous row
            idx -= 1

        # if current capacity is zero
        # we found all the items
        if jdx == 0:
            break

    # because, we built sequence using backtracking, we reverse it
    sequence.reverse()

    return [dp[-1][-1], sequence]

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
