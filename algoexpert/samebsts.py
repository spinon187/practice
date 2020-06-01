def sameBsts(arrayOne, arrayTwo):
  if len(arrayOne) != len(arrayTwo):
    return False
  elif len(arrayOne) == 0 and len(arrayTwo) == 0:
    return True
  rootOne, rootTwo = arrayOne[0], arrayTwo[0]
  if rootOne != rootTwo:
    return False
  bigOne, smallOne = fillArrays(arrayOne, rootOne)
  bigTwo, smallTwo = fillArrays(arrayTwo, rootTwo)
  return sameBsts(bigOne, bigTwo) and sameBsts(smallOne, smallTwo)

def fillArrays(array, rootVal):
	if len(array) == 0:
		return [[],[]]
	small = []
	big = []
	for i in range(1, len(array)):
		if array[i] < rootVal:
			small.append(array[i])
		else:
			big.append(array[i])
	return [big, small]
	