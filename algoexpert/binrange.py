def searchForRange(array, target):
  hit = -1
  first = -1
  last = -1
  l = 0
  r = len(array)-1
  while l <= r and hit < 0:
    m = (l+r)//2
    if array[m] == target:
      hit = m
    elif target < array[m]:
      r = m-1
    else:
      l = m+1
  if hit >= 0:
    if hit == 0 or array[hit] != array[hit-1]:
      first = hit
    else:
      l = 0
      r = hit-1
      while l <= r and first < 0:
        m = (l+r)//2
        if array[m] == target:
          if m == 0 or array[m-1] != target:
            first = m
          else:
            r = m-1
        else:
          if array[m+1] == target:
            first = m+1
          else:
            l = m+1
    if hit == len(array)-1 or array[hit] != array[hit+1]:
      last = hit
    else:
      l = hit+1
      r = len(array)-1
      while l<=r and last < 0:
        m = (l+r)//2
        if array[m] == target:
          if m == len(array)-1 or array[m+1] != target:
            last = m
          else:
            l = m+1
        else:
          if array[m-1] == target:
            last = m-1
          else:
            r = m-1
  return [first, last]