def shiftedBinarySearch(array, target):
  l = 0
  r = len(array)-1
  while l <= r:
    m = (l+r)//2
    if array[m] == target:
      return m
    if array[l] <= array[m]:
      if target >= array[l] and target < array[m]:
        r = m-1
      else:
        l = m+1
    elif target > array[m] and target <= array[r]:
      l = m+1
    else:
      r = m-1
      
  return -1