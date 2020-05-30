def powerset(array):
  output = [[]]
	for x in array:
		for i in range(len(output)):
			output.append(output[i] + [x])
	return output