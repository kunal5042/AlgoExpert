import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        try:
            self.assertEqual(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])
            print("Test Case 1: Passed")
        except:
            print("Test Case 1: Failed")
            
    def test_case_2(self):
        try:
            self.assertEqual(subarraySort([1, 2]), [-1, -1])
            print("Test Case 2: Passed")
        except:
            print("Test Case 2: Failed")
            
    def test_case_3(self):
        try:
            self.assertEqual(subarraySort([2, 1]), [0, 1])
            print("Test Case 3: Passed")
        except:
            print("Test Case 3: Failed")
            
    def test_case_4(self):
        try:
            self.assertEqual(subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]), [0, 11])
            print("Test Case 4: Passed")
        except:
            print("Test Case 4: Failed")
            
    def test_case_5(self):
        try:
            self.assertEqual(subarraySort([1, 2, 4, 7, 8, 9, 10, 11, 12, 15]), [-1, -1])
            print("Test Case 5: Passed")
        except:
            print("Test Case 5: Failed")
        

def subarraySort(array):
    minimax = [None, None]

    for idx in range(len(array)):
        if idx == 0:
            if array[idx+1] < array[idx]:
                minimax[0] = 0
                minimax[1] = 0
            continue

        if idx == len(array)-1:
            if array[idx-1] > array[idx]:
                if minimax[0] is None:
                    minimax[0] = idx
                    minimax[1] = idx
                    
                if array[minimax[0]] > array[idx]:
                    minimax[0] = idx
                    
                if array[minimax[1]] < array[idx]:
                    minimax[1] = idx
            continue

        check(array, idx, minimax)

    if minimax[0] is None: return [-1, -1]

    smaller = array[minimax[0]]
    smalidx = 0

    for ele in array:
        if ele <= smaller:
            smalidx += 1
        else:
            break

    larger = array[minimax[1]]
    laridx = len(array)-1

    while array[laridx] >= larger:
            laridx -= 1

    return [smalidx, laridx]




def check(array, idx, minimax):
    if array[idx-1] > array[idx] or array[idx] > array[idx+1]:
        if minimax[0] is None:
            minimax[0] = idx
            minimax[1] = idx
        else:
            if array[minimax[0]] > array[idx]:
                minimax[0] = idx

            if array[minimax[1]] < array[idx]:
                minimax[1] = idx
                


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    tester.test_case_2()
    tester.test_case_3()
    tester.test_case_4()
    tester.test_case_5()
# Kunal Wadhwa
