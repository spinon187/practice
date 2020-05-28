def maxSubsetSumNoAdjacent(array):
  if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	second = array[0]
	first = max(array[1], second)
	for x in range(2, len(array)):
		current = max(first, second + array[x])
		second = first
		first = current
	return first