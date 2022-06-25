'''
Explanation
Since the given array is a sorted,we figure out that 3 cases are possible 
1. index > ar[index]
2. index < ar[index]
3. index == ar[index]

Case 1 : 
Eg [5 -3 0 3 4 5 9]
      0   1 2 3 4 5 6
Since the index is greater than the value, we can observe that index == ar[index] can only be to the right of the array. Hence l = mid+1

Case 2:
Eg [5 -3 0 3 4 5 9]
      0   1 2 3 4 5 6
Since the index is less than the value, we can observe that index == ar[index] can only be to the left of the array. Hence r = mid - 1

Case 3:
Eg [5 -3 0 3 4 5 9]
      0   1 2 3 4 5 6
For this case let's say l = 3, r = 5, mid = 4 (mid = (i+j)/2) . We find that mid == ar[mid], hence we set our ans to mid . 

Now the question is, which direction do I move my left and right pointers to? Since there can be multiple indices which can satisfy the property.
 
Acc to the question, we have to find the least index possible which satisfies the property index == ar[index]. Hence our window [ l,r ] should be shifted towards left which makes sure that we get lesser value of mid in the next iterations. Hence r = mid -1. 

Putting it all together, we get the solution
'''


'''
O(log(n)) Time and O(1) Space
'''
def indexEqualsValue(array):
    def helper(left, right, result):
        while left <= right:
            middle = left + (right-left) // 2
    
            if array[middle] == middle:
                result = min(result, middle)
                right = middle - 1
    
            elif array[middle] > middle:
                right = middle - 1
    
            else:
                left = middle + 1
        return result

    result = helper(0, len(array)-1, float('inf'))

    return result if result != float('inf') else -1

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-5, -3, 0, 3, 4, 5, 9]
        expected = 3
        actual = indexEqualsValue(array)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa