def subarraySort(array):
  low = float('inf')
  high = float('-inf')
  start = -1
  end = -1
  for i in range(1, len(array)):
    if array[i] < array[i-1]:
      low = min(low, array[i])
      high = max(high, array[i-1])
  for i in range(len(array)):
    if start < 0:
      if array[i] > low:
        start = i
    if start >= 0 and end < 0:
      if array[i] > high:
        end = i-1
      elif i == len(array) - 1:
        end = len(array) - 1
  return [start, end]