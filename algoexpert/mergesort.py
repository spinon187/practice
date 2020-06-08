def mergeSort(array):
	if len(array) <= 1:
		return array
	aux = array[:]
	msHelper(array, aux, 0, len(array)-1)
	return array

def msHelper(main, aux, start, end):
	if start == end:
		return
	middle = (start + end) // 2
	msHelper(aux, main, start, middle)
	msHelper(aux, main, middle+1, end)
	merge(main, aux, start, middle, end)
	
def merge(main, aux, start, middle, end):
	k = start
	i = start
	j = middle+1
	while i <= middle and j <= end:
		if aux[i] <= aux[j]:
			main[k] = aux[i]
			i += 1
		else:
			main[k] = aux[j]
			j += 1
		k += 1
	while i <= middle:
		main[k] = aux[i]
		i += 1
		k += 1
	while j <= end:
		main[k] = aux[j]
		j += 1
		k += 1