def isMonotonic(array):
  plus = None
	for x in range(1, len(array)):
		if plus is None:
			if array[x] < array[x-1]:
				plus = False
			elif array[x] > array[x-1]:
				plus = True
		elif plus is True:
			if array[x] < array[x-1]:
				return False
		elif plus is False:
			if array[x] > array[x-1]:
				return False
	return True