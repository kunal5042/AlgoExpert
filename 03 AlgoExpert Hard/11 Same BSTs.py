import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.assertEqual(sameBsts(arrayOne, arrayTwo), True)
        print("Test Case: Passed")


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    # Logic
    # The order in which we insert elements in the left and right subtree should be same 
    left_one = get_smaller(arrayOne)
    left_two = get_smaller(arrayTwo)
    right_one = get_bigger_or_equal(arrayOne)
    right_two = get_bigger_or_equal(arrayTwo)

    return sameBsts(left_one, left_two) \
    and sameBsts(right_one, right_two)


def get_smaller(arr):
    smaller = []
    for idx in range(1, len(arr)):
        if arr[idx] < arr[0]:
            smaller.append(arr[idx])

    return smaller


def get_bigger_or_equal(arr):
    bigger = []
    for idx in range(1, len(arr)):
        if arr[idx] >= arr[0]:
            bigger.append(arr[idx])

    return bigger

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa