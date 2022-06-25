'''
O(n log(k)) Time and O(k) Space: where n is the length of the input array
'''
def sortKSortedArray(array, k):
    heap = MinHeap()
    for idx in range(k+1):
        if idx < len(array):
            heap.insert(array[idx])

    next_insertion = k+1
    for idx in range(len(array)):
        array[idx] = heap.remove()
        if next_insertion < len(array):
            heap.insert(array[next_insertion])
            next_insertion += 1

    return array


class MinHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self):
        node = len(self) - 1
        parent = (node - 1 ) // 2
        while parent >= 0:
            if self.heap[node] < self.heap[parent]:
                self.swap(node, parent)

                node = parent
                parent = (node-1) // 2
            else:
                break

    def sift_down(self):
        node = 0
        child_one = (2*node) + 1
        while child_one < len(self):
            if (2*node) + 2 < len(self):
                child_two = (2*node)+2
            else:
                child_two = None

            if child_two is not None:
                if self.smaller(child_one, child_two):
                    compare_with = child_one
                else:
                    compare_with = child_two

            else:
                compare_with = child_one


            if self.smaller(node, compare_with):
                break
            else:
                self.swap(node, compare_with)
                node = compare_with
                child_one = (2*node) + 1

    def remove(self):
        if len(self) == 1:
            return self.heap.pop()
        if len(self) > 1:
            self.swap(0, len(self)-1)
            to_return = self.heap.pop()
            self.sift_down()
            return to_return
        else:
            return 'Heap Empty'

    def insert(self, val):
        self.heap.append(val)
        self.sift_up()

    def __len__(self):
        return len(self.heap)

    def swap(self, idx, jdx):
        self.heap[idx], self.heap[jdx] = \
        self.heap[jdx], self.heap[idx]

    def smaller(self, idx, jdx):
        if self.heap[idx] < self.heap[jdx]:
            return True
        else:
            return False


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 2, 1, 5, 4, 7, 6, 5]
        k = 3
        expected = [1, 2, 3, 4, 5, 5, 6, 7]
        actual = sortKSortedArray(input, k)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa