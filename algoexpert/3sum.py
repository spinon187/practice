def threeNumberSum(array, targetSum):
  output = []
	array.sort()
	for x in range(len(array)):
		remaining = targetSum - array[x]
		y = x+1
		z = len(array)-1
		while y<z:
			if remaining == array[y] + array[z]:
				output.append([array[x], array[y], array[z]])
				y += 1
				z -= 1
			elif remaining < array[y] + array[z]:
				z -= 1
			else:
				y += 1
	return output