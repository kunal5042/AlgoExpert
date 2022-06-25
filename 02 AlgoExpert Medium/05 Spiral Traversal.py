def spiralTraverse(array):
	spiral_traversal = []
	
	increasing_row, increasing_col = 0, 0
	decreasing_row, decreasing_col = len(array) - 1, len(array[0]) - 1
	
	while increasing_row <= decreasing_row and increasing_col <= decreasing_col:
		for col in range(increasing_col, decreasing_col + 1):
			spiral_traversal.append(array[increasing_row][col])
			
		for row in range(increasing_row + 1, decreasing_row + 1):
			spiral_traversal.append(array[row][decreasing_col])
			
		for col in reversed(range(increasing_col, decreasing_col)):
			if increasing_row == decreasing_row:
				break
			spiral_traversal.append(array[decreasing_row][col])
		
		for row in reversed(range(increasing_row + 1, decreasing_row)):
			if increasing_col ==  decreasing_col:
				break
			spiral_traversal.append(array[row][increasing_col])
		
		increasing_col += 1
		decreasing_col -= 1
		increasing_row += 1
		decreasing_row -= 1
	
	return spiral_traversal

# Kunal Wadhwa
