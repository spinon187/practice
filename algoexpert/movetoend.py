def moveElementToEnd(array, toMove):
  i = len(array)-1
	j = len(array)-1
	while i >= 0:
		if array[i] == toMove:
			if i == j:
				i -= 1
				j -= 1
			else:
				array[i], array[j] = array[j], array[i]
				i -= 1
				j -= 1
		else:
			i -= 1
	return array