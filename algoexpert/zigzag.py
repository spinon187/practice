def zigzagTraverse(array):
	if len(array) == 1:
		return array[0]
	final = []
	final.append(array[0][0])
	upHelper(array, final, 1, 0, len(array)-1, len(array[0])-1)
	return final

def upHelper(array, output, row, col, height, width):
	output.append(array[row][col])
	if col == width and row == height:
		return
	while row > 0 and col < width:
		row -= 1
		col += 1
		output.append(array[row][col])
	if row == 0:
		if col == width:
			downHelper(array, output, row+1, col, height, width)
		else:
			downHelper(array, output, row, col+1, height, width)
	elif col == width:
		downHelper(array, output, row+1, col, height, width)

			
def downHelper(array, output, row, col, height, width):
	output.append(array[row][col])
	if col == width and row == height:
		return
	while row < height and col > 0:
		row += 1
		col -= 1
		output.append(array[row][col])
	if col == 0:
		if row == height:
			upHelper(array, output, row, col+1, height, width)
		else:
			upHelper(array, output, row+1, col, height, width)
	elif row == height:
		upHelper(array, output, row, col+1, height, width)
