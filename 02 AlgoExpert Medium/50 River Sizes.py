# https://www.algoexpert.io/questions/river-sizes
# Graphs

'''
   O(wh) Time and O(wh) Space
   BFS Solution
'''
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

'''Another Solution'''
# GLOBAL VARIABLE
river_size = 0
def riverSizes(matrix):
	visited = [[False for value in row] for row in matrix]
	result = []
	
	for row_no, row_list in enumerate(matrix):
		for col_no, value_in_row in enumerate(matrix[row_no]):
			if not visited[row_no][col_no]:
				if matrix[row_no][col_no] == 1:
					global river_size
					river_size = 1
					visited[row_no][col_no] = True
					found_a_one(row_no, col_no, matrix, visited)
					result.append(river_size)
	return result
			


def found_a_one(row_number, col_number, matrix, visited):
	global river_size
	up_index = row_number - 1 if row_number - 1 >= 0 else None
	down_index = row_number + 1 if row_number + 1 < len(matrix) else None
	left_index = col_number - 1 if col_number - 1 >= 0 else None
	right_index = col_number + 1 if col_number + 1 < len(matrix[row_number]) else None
	go_up, go_down, go_left, go_right = False, False, False, False
	
	if up_index is not None:
		# visit the element 
		if not visited[up_index][col_number]:
			visited[up_index][col_number] = True
			if matrix[up_index][col_number] == 1:
				river_size += 1
				print(f'Visited [{up_index}][{col_number}]: Size = {river_size}')
				found_a_one(up_index, col_number, matrix, visited)
	
	if down_index is not None:
		if not visited[down_index][col_number]:
			visited[down_index][col_number] = True
			if matrix[down_index][col_number] == 1:
				river_size += 1
				print(f'Visited [{down_index}][{col_number}]: Size = {river_size}')
				found_a_one(down_index, col_number, matrix, visited)
	
	if left_index is not None:
		if not visited[row_number][left_index]:
			visited[row_number][left_index] = True
			if matrix[row_number][left_index] == 1:
				river_size += 1
				print(f'Visited [{row_number}][{left_index}]: Size = {river_size}')
				found_a_one(row_number, left_index, matrix, visited)
				
	if right_index is not None:
		if not visited[row_number][right_index]:
			visited[row_number][right_index] = True
			if matrix[row_number][right_index] == 1:
				river_size += 1
				print(f'Visited [{row_number}][{right_index}]: Size = {river_size}')
				found_a_one(row_number, right_index, matrix, visited)	


def get_adjacents(result, x, y, height, width):
    if x - 1 >= 0:
        result.append((x-1,y))
    if x + 1 < height:
        result.append((x+1,y))
    if y - 1 >= 0:
        result.append((x, y-1))
    if y + 1 < width:
        result.append((x, y+1))
                            


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa


'''