def longestIncreasingSubsequence(array):
  sequences = [None for _ in array]
  indices = [None for _ in range(len(array)+1)]
  length = 0
  
  for idx, value in enumerate(array):
    newLength = binSrch(1, length, indices, array, value)
    sequences[idx] = indices[newLength - 1]
    indices[newLength] = idx
    length = max(length, newLength)
    
  return buildSeq(array, sequences, indices[length])

    
def binSrch(start, end, indices, array, value):
  if start > end:
    return start
  mid = (start+end) // 2
  if array[indices[mid]] < value:
    start = mid + 1
  else:
    end = mid - 1
  return binSrch(start, end, indices, array, value)

def buildSeq(array, sequences, current):
  sequence = []
  while current is not None:
    sequence.append(array[current])
    current = sequences[current]
  return list(reversed(sequence))