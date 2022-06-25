'''
O(n) Time and Space: where n is the length of the input array
'''
def maximizeExpression(array):
    # base case
    if len(array) < 4: return 0

    # divided expression into subproblems which will be calculated one by one
    max_a = [ele for ele in array]
    max_a_minus_b = [float('-inf') for ele in array]
    max_a_minus_b_plus_c = [float('-inf') for ele in array]
    max_expression = [float('-inf') for ele in array]
    
    for idx in range(1, len(array)):
        max_a[idx] = max(max_a[idx-1], array[idx])

    for idx in range(1, len(array)):
        max_a_minus_b[idx] = max(max_a[idx-1] - array[idx], max_a_minus_b[idx-1])

    for idx in range(2, len(array)):
        max_a_minus_b_plus_c[idx] = max(max_a_minus_b[idx-1] + array[idx], max_a_minus_b_plus_c[idx-1])

    for idx in range(3, len(array)):
        max_expression[idx] = max(max_a_minus_b_plus_c[idx-1] - array[idx], max_expression[idx-1])

    print(max_a)
    print(max_a_minus_b)
    print(max_a_minus_b_plus_c)
    print(max_expression)
    return max_expression[-1] if max_expression[-1] != float('-inf') else 0


'''
Expression: array[a] - array[b] + array[c] - array[d]
a, b, c, d: are indices that satisfy the relation -> ( a < b < c < d )

Goal: Maximize the result of the expression
Sub-Goals:
    - Maximize the values of array[a] and array[c]
    - Minimize the values of array[b] and array[d]

Brute Force: Pick all valid combinations for a,b,c,d, evaluate the expression and keep track of the maximum


Can we achieve our sub-goals in steps?
Can we use the result of each sub-problem for solving the bigger problem?
A: Yes

How?
A:
    - We start by maximizing the value of array[a] for every index
    - We find the maximum value of array[a] - array[b] for every index using the array we built in previous step
    - We find the maximum value of array[a] - array[b] + array[c] for every index using array built in previous step
    - Finally we find the maximum value of the expression by finding maximum value of array[a] - array[b] + array[c] - array[d] for every index

'''

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 6, 1, -3, 2, 7]
        expected = 4
        actual = maximizeExpression(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa