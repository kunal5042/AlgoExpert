# https://www.algoexpert.io/questions/minimum-passes-of-matrix
# Graphs

from collections import deque
'''Solution - 1'''
'''O(w * h) time | O(w * h) space - where w is the width of the matrix and h is the height'''
def minimumPassesOfMatrix(matrix):
    queue = deque()
    height, width = len(matrix), len(matrix[0])
    for x in range(height):
        for y in range(width):
            if matrix[x][y] > 0:
                # put all the positive elements in the queue for later processing
                queue.append((x,y))
    
    # if not even single +ve value is found, we can't do anything
    if len(queue) == 0:
        return -1
    # helper function to return all adjacent 
    def get_negative_adjacents(cx, cy, cq):
        if cx + 1 >= 0 and cx + 1 < height:
            if matrix[cx+1][cy] < 0:
                cq.append((cx+1, cy))

        if cx - 1 >= 0 and cx - 1 < height:
            if matrix[cx-1][cy] < 0:
                cq.append((cx-1, cy))

        if cy + 1 >= 0 and cy + 1 < width:
            if matrix[cx][cy+1] < 0:
                cq.append((cx, cy+1))

        if cy - 1 >= 0 and cy - 1 < width:
            if matrix[cx][cy-1] < 0:
                cq.append((cx, cy-1))

    passes = 0
    while len(queue) != 0:
        # this count tell us how many positive elements we have in the matrix for this pass
        count = len(queue)
        for _ in range(count):
            # we take all these positive elements out, one by one
            (px, py) = queue.popleft()

            # find all their negative neighbours
            negative_neighbours = []
            get_negative_adjacents(px, py, negative_neighbours)

            # convert those negative neihbours into positive and add these converted positive elements in the queue
            # for the next phase of processing
            for (nx, ny) in negative_neighbours:
                if matrix[nx][ny] < 0: matrix[nx][ny] *= -1
                # add the converted elements into queue
                queue.append((nx,ny))

        # next phase
        passes += 1

    for x in range(height):
        for y in range(width):
            if matrix[x][y] < 0:
                return -1

    # The last level of processsing is not a phase but a check
    return passes-1

'''Solution - 2'''
'''O(w * h) time | O(w * h) space - where w is the width of the matrix and h is the height'''
def minimumPassesOfMatrix(matrix):
    q1, q2  = deque(), deque()
    height, width = len(matrix), len(matrix[0])
    for x in range(height):
        for y in range(width):
            if matrix[x][y] > 0:
                q1.append((x,y))

    # if not even single +ve value is found, we can't do anything
    if len(q1) == 0:
        return -1

    def get_negative_adjacents(cx, cy, cq):
        if cx + 1 >= 0 and cx + 1 < height:
            if matrix[cx+1][cy] < 0:
                cq.append((cx+1, cy))

        if cx - 1 >= 0 and cx - 1 < height:
            if matrix[cx-1][cy] < 0:
                cq.append((cx-1, cy))

        if cy + 1 >= 0 and cy + 1 < width:
            if matrix[cx][cy+1] < 0:
                cq.append((cx, cy+1))

        if cy - 1 >= 0 and cy - 1 < width:
            if matrix[cx][cy-1] < 0:
                cq.append((cx, cy-1))


    passes = 0
    while len(q1) != 0 or len(q2) != 0:
        if passes % 2 == 0:
            current_queue   = q1
            auxiliary_queue = q2
        else:
            current_queue   = q2
            auxiliary_queue = q1

        count = len(current_queue)
        for _ in range(count):
            (px, py) = current_queue.popleft()
            
            negative_neighbours = []
            get_negative_adjacents(px, py, negative_neighbours)
            
            for (nx, ny) in negative_neighbours:
                if matrix[nx][ny] < 0: matrix[nx][ny] *= -1
                auxiliary_queue.append((nx,ny))

        passes += 1

    for x in range(height):
        for y in range(width):
            if matrix[x][y] < 0:
                return -1

    return passes-1



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)

            
        
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''