def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
	arrayTwo.sort()
	closestPair = [float('inf'), float('-inf')]
	pointerOne = 0
	pointerTwo = 0
	while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
		if abs(closestPair[0] - closestPair[1]) > abs(arrayOne[pointerOne] - arrayTwo[pointerTwo]):
			closestPair = [arrayOne[pointerOne], arrayTwo[pointerTwo]]
		if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
			pointerOne += 1
		elif arrayOne[pointerOne] > arrayTwo[pointerTwo]:
			pointerTwo += 1
		elif arrayOne[pointerOne] == arrayTwo[pointerTwo]:
			return [arrayOne[pointerOne], arrayTwo[pointerTwo]]
	return closestPair