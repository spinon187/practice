def riverSizes(matrix):
  visited = set()
	lengths = []
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 1 and (row, col) not in visited:
				lengths.append(traceRiver(matrix, row, col, visited))
	return lengths


def traceRiver(matrix, row, col, visited):
	if (row, col) in visited:
		return 0
	visited.add((row, col))
	count = 0
	if matrix[row][col] == 1:
		count += 1
		if row > 0:
			count += traceRiver(matrix, row-1, col, visited)
		if row < len(matrix)-1:
			count += traceRiver(matrix, row+1, col, visited)
		if col > 0:
			count += traceRiver(matrix, row, col-1, visited)
		if col < len(matrix[0])-1:
			count += traceRiver(matrix, row, col+1, visited)
	return count