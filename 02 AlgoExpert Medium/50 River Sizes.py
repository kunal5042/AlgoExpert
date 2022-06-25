import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)
        print("Test Case: Passed")
        

'''O(wh) Time and O(wh) Space: where w is the width and h is the height of the given matrix'''
def riverSizes(matrix):
    (width, height) = (len(matrix[0]), len(matrix))
    # to keep track of visited cells in the matrix
    visited = [[False for x in range(width)] for y in range(height)]
    result = []

    # a hash map of co-ordinates of all the cells that are ones
    ones_coordinates = {}
    for x in range(height):
        for y in range(width):
            if matrix[x][y] == 1:
                # if a cell has value == 1, put it's co-ordinates in the map
                ones_coordinates[(x,y)] = (x,y)

    for x in range(height):
        for y in range(width):
            # if current cell has value 1 and it has not yet been visited
            if matrix[x][y] == 1:
                if visited[x][y] is True:
                    continue

                # mark it as visited
                visited[x][y] = True
                # river size = 1
                current_river_size = 1

                # get it's adjacents cells in all directions
                adjacents = []
                get_adjacents(adjacents, x, y, height, width)

                # as long as all the adjacent cells and their adjacent cells have not been checked
                while len(adjacents) > 0:
                    # keep checking adjacent cell one at a time
                    adj = adjacents.pop(0)
                    # if the adjacent cell has value = 1
                    if adj in ones_coordinates:
                        current_adjacent = ones_coordinates[adj]
                        current_adjacent_x = current_adjacent[0]
                        current_adjacent_y = current_adjacent[1]

                        # and it has not yet been visited
                        if visited[current_adjacent_x][current_adjacent_y] is False:
                            # increment the current river size
                            current_river_size += 1
                            # mark it as visited
                            visited[current_adjacent_x][current_adjacent_y] = True
                            # add it's adjacents the queue
                            get_adjacents(adjacents, current_adjacent_x, current_adjacent_y, height, width)

                # any river size >= 1 is valid, add it to the result
                if current_river_size >= 1:
                    result.append(current_river_size)

    return result


def get_adjacents(result, x, y, height, width):
    if x - 1 >= 0:
        result.append((x-1,y))
    if x + 1 < height:
        result.append((x+1,y))
    if y - 1 >= 0:
        result.append((x, y-1))
    if y + 1 < width:
        result.append((x, y+1))

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()

# Kunal Wadhwa  
