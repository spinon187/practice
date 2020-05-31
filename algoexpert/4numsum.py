def fourNumberSum(array, targetSum):
  vals = {}
  final = []
  for i in range(1, len(array)-1):
    for j in range(i+1, len(array)):
      curr = array[i] + array[j]
      diff = targetSum - curr
      if diff in vals:
        for d in vals[diff]:
          final.append(d + [array[i], array[j]])
    for k in range(0, i):
      curr = array[i] + array[k]
      if curr not in vals:
        vals[curr] = []
      vals[curr].append([array[i], array[k]])
  return final