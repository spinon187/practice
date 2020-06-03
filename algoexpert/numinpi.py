def numbersInPi(pi, numbers):
  table = {number: True for number in numbers}
  minSpaces = getMin(pi, table, {}, 0)
  return -1 if minSpaces == float('inf') else minSpaces
  
def getMin(pi, table, cache, x):
  if x == len(pi):
    return -1
  if x in cache:
    return cache[x]
  minSpaces = float('inf')
  for i in range(x, len(pi)):
    prefix = pi[x:i+1]
    if prefix in table:
      minSpaces = min(minSpaces, getMin(pi, table, cache, i+1) + 1)
  cache[x] = minSpaces
  return cache[x]
