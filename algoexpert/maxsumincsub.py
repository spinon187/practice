def maxSumIncreasingSubsequence(array):
  sums = []
  seq = [None for x in array]
  maxVal = float('-inf')
  maxIdx = None
  for x in range(len(array)):
    curr = array[x]
    runningMax = curr
    pointer = None
    for y in range(x):
      if curr > array[y]:
        if runningMax < sums[y] + curr:
          pointer = y
          runningMax = sums[y] + curr
    seq[x] = pointer
    sums.append(runningMax)
    if maxVal < runningMax:
      maxVal = runningMax
      maxIdx = x
  output = []
  while maxIdx != None:
    output.append(array[maxIdx])
    maxIdx = seq[maxIdx]
  return [maxVal, list(reversed(output))]