def quickSort(array):
  qsHelper(0, len(array)-1, array)
  return array

def qsHelper(start, end, array):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    if array[left] > array[pivot] and array[right] < array[pivot]:
      array[left], array[right] = array[right], array[left]
    if array[left] <= array[pivot]:
      left += 1
    if array[right] >= array[pivot]:
      right -= 1
  array[pivot], array[right] = array[right], array[pivot]
  if (right-1) - start < end - (right+1):
    qsHelper(start, right-1, array)
    qsHelper(right+1, end, array)
  else:
    qsHelper(right+1, end, array)
    qsHelper(start, right-1, array)