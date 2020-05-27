def longestPeak(array):
  up = 0
	down = 0
	longest = 0
	for i in range(1, len(array)):
		if array[i-1] < array[i]:
			if up >= 2 and down >=1:
				longest = max(longest, up+down)
				up = 2
			elif up == 0:
				up += 2
			else:
				up +=1
			down = 0
		elif array[i-1] > array[i]:
			if up >= 2:
				down += 1
			else:
				down = 0
				up = 0
		elif array[i-1] == array[i]:
			if up >= 2 and down >= 1:
				longest = max(longest, up+down)
			up = 0
			down = 0
	if up >=2 and down >= 1:
		longest = max(longest, up+down)
	return longest