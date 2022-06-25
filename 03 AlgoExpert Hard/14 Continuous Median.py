import heapq
# '''
# The Idea:
#     - To calculate median, we need the middle or middle two elements at any given point of time
#     - We divide our array/data structure into two parts, the lower half and the upper half, and store them separately
#     - The lower half elements are stored in maximum first fashion ( Max Heap )
#     - The upper half elements are stored in minimum first fashion ( Min Heap )
#     - Now, at any given point of time, we can compute the median by accessing the maximum of lower half and minimum of upper half in O(1) time
#     - The insertion and balancing of the data structures and the computation of median is explained in the respective defined functions.
# '''
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.lower_half = MaxHeap()
        self.upper_half = MinHeap()

    def insert(self, number):
    # '''
    #     If both heaps are empty, we start by inserting in the lower half
    #     Another thing we check is, if the number we are trying to insert is less than the maximum of the lower half
    #     Then, it belongs in the lower half, otherwise we insert it in the upper half
    # '''
        if len(self.lower_half) == 0 or number < self.lower_half.peek():
            self.lower_half.insert(number) 
        else:
            self.upper_half.insert(number)
# '''
#         Now, we might end up inserting more elements in one half than the other
#         But, we need to keep them as close in length as possible, coz only then we can get the median
#         As their name state *half*
#         Hence, after every insertion we rebalance the heaps based on this condition
#         if abs(len(lower_half) - len(upper_half)) > 1
# '''
        self.rebalance_heaps()

    def rebalance_heaps(self):
# '''
#         As stated earlier, if heaps need to be rebalanced, we pop the top element from the larger heap
#         and insert it in the smaller heap
# '''
        if abs(len(self.lower_half) - len(self.upper_half)) > 1:
            if len(self.lower_half) > len(self.upper_half):
                self.upper_half.insert(self.lower_half.remove())
            else:
                self.lower_half.insert(self.upper_half.remove())

# '''
#         Once the halves are balanced, we can safely compute median.
# '''
        self.update_median()

# '''
#         Here, two things can happen
#         1. Total elements are even, in that case we take maximum ele of lower half and minimum ele of upper half for the computation
#         2. Total elements are odd, we take the root node of the half whose length is bigger for the computation
# '''
    def update_median(self):
        if len(self.lower_half) == len(self.upper_half):
            self.median = (self.upper_half.peek() + self.lower_half.peek()) / 2
        else:
            if len(self.lower_half) > len(self.upper_half):
                self.median = self.lower_half.peek()
            else:
                self.median = self.upper_half.peek()

    def getMedian(self):
        print(self.lower_half)
        print(self.upper_half)
        return self.median

# '''
# Max Heap Implementation
# '''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self):
        child_idx = len(self.heap)-1
        parent_idx = (len(self.heap)-1)//2
        while parent_idx >= 0:
            if self.heap[parent_idx] < self.heap[child_idx]:
                self.swap(parent_idx, child_idx)
                child_idx = parent_idx
                parent_idx = (child_idx-1)//2
            else:
                break

    def sift_down(self, node_idx):
        endidx = len(self.heap)-1
        child_one = (2 * node_idx ) + 1
        while child_one < endidx:
            child_two = (2 * node_idx) + 2 if (2 * node_idx) + 2 < endidx else None
            
            if child_two is not None:
                if self.heap[child_one] > self.heap[child_two]:
                    to_compare_with = child_one
                else:
                    to_compare_with = child_two
            else:
                to_compare_with = child_one
                
            if self.heap[node_idx] < self.heap[to_compare_with]:
                self.swap(node_idx, to_compare_with)
                
                node_idx = to_compare_with
                child_one = (2 * node_idx) + 1
            
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1)
        maximum_ele = self.heap.pop()
        self.sift_down(0)
        return maximum_ele

    def insert(self, value):
        self.heap.append(value)
        self.sift_up()

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def __str__(self):
        return str(self.heap)
        
    def __len__(self):
        return len(self.heap)

# '''
# Min Heap Implementation Using heapq module
# '''
class MinHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        
    def insert(self, value):
        heapq.heappush(self.heap, value)
        
    def remove(self):
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0] if len(self.heap) > 0 else 'Empty'

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)


# Kunal Wadhwa