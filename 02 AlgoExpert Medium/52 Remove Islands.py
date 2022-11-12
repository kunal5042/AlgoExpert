# https://www.algoexpert.io/questions/remove-islands
# Graphs

def removeIslands(matrix):
    (width, height) = (len(matrix[0]), len(matrix))
    # to keep track of visited cells in the matrix
    visited = [[False for x in range(width)] for y in range(height)]
    result = []

    # a hash map of co-ordinates of all the cells that are ones
    # we include the border ones too, because we wanna find out which cells are adjacent with border ones
    # as they don't qualify for being an island
    ones_coordinates = {}
    for x in range(height):
        for y in range(width):
            if matrix[x][y] == 1:
                # if a cell has value == 1, put it's co-ordinates in the map
                ones_coordinates[(x,y)] = (x,y)

    for x in range(height):
        for y in range(width):
            # if current cell has not been visited
            # does not touch the border
            # and it's value is 1
            # it can be a potential island and we process only these kind of elements
            if matrix[x][y] == 1 and touching_border((x,y), height, width) is False and visited[x][y] is False:

                # mark it as visited
                visited[x][y] = True
                # currently it's a valid island
                is_island = True
                # we will use this list to remove the island
                island_coordinates = [(x,y)]

                # get it's adjacents cells in all directions
                adjacents = []
                get_adjacents(adjacents, x, y, height, width)

                # This loop runs as long as adjacents of adjacents of adjacents exist, once we reach a stage
                # that there are no more valid adjacent cells, we stop
                # and inside this loop we process all of these adjacents cells
                while len(adjacents) > 0:
                    # keep checking adjacent cell one at a time
                    adj = adjacents.pop(0)
                    # if the adjacent cell has value = 1
                    # this means, it can extend the island but only if it doesn't touch the border
                    if adj in ones_coordinates:
                        current_adjacent = ones_coordinates[adj]
                        current_adjacent_x = current_adjacent[0]
                        current_adjacent_y = current_adjacent[1]

                        # if any of the adjacent cells touch the border
                        # means this entire list of connected cells is not a valid island
                        # we do not break at this stage, because we need to find all the remaining cells which are connected these cells
                        # and mark them visited, so that this entired connected chain can be excluded from processing
                        # by the visited check in the inner loop
                        if touching_border((current_adjacent_x, current_adjacent_y), height, width) is True:
                            is_island = False

                        # if cells are not touching the border, we keep a track of their coordinates for removal
                        if visited[current_adjacent_x][current_adjacent_y] is False:
                            # add it's coordinates to the island_coordinates
                            island_coordinates.append((current_adjacent_x, current_adjacent_y))
                            # mark it as visited
                            visited[current_adjacent_x][current_adjacent_y] = True
                            # and add it's adjacents the queue
                            get_adjacents(adjacents, current_adjacent_x, current_adjacent_y, height, width)

                # if after all the processing, we find that this current chain of connected cells 
                # form a valid island
                # we remove this island
                if is_island is True:
                    while len(island_coordinates) > 0:
                        (x,y) = island_coordinates.pop()
                        matrix[x][y] = 0
    # return the modified matrix
    return matrix

# helper function to get adjacents in all directions
def get_adjacents(result, x, y, height, width):
    # x represents rows, y represents columns
    if x - 1 >= 0:
        result.append((x-1,y))
    if x + 1 < height:
        result.append((x+1,y))
    if y - 1 >= 0:
        result.append((x, y-1))
    if y + 1 < width:
        result.append((x, y+1))

# helper function to determine if current cell with coordinates equal to coordinates 
# is a border cell or not
def touching_border(coordinates, height, width):
    if coordinates[0] == 0 or coordinates[0] == height - 1:
        return True
    if coordinates[1] == 0 or coordinates[1] == width - 1:
        return True
    return False



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        actual = removeIslands(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''