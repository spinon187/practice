def quickselect(array, k):
	target = k-1
	start = 0
	end = len(array)-1
	while True:
		pivot = start
		left = start+1
		right = end
		while left <= right:
			if array[left] > array[pivot] and array[right] < array[pivot]:
				array[right], array[left] = array[left], array[right]
			if array[left] <= array[pivot]:
				left += 1
			if array[right] >= array[pivot]:
				right -= 1
		array[right], array[pivot] = array[pivot], array[right]
		if right == target:
			return array[right]
		elif right < target:
			start = right+1
		else:
			end = right-1