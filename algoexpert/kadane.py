def kadanesAlgorithm(array):
  maxSum = float('-inf')
	running = None
	for x in array:
		if running is None:
			running = x
			maxSum = x
		elif x < 0:
			if x > maxSum:
				maxSum = x
			elif running + x <= 0:
				running = 0
			else: running += x
		else:
			running += x
			maxSum = max(running, maxSum)
	return maxSum