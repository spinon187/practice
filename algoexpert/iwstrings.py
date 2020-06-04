def interweavingStrings(one, two, three):
  if len(three) != len(one) + len(two):
    return False
  cache = [[None for x in range(len(two)+1)] for y in range(len(one)+1)]
  return compare(one, two, three, 0, 0, cache)

def compare(one, two, three, i, j, cache):
  if cache[i][j] is not None:
    return cache[i][j]
  k = i+j
  if k == len(three):
    return True
  if i < len(one) and one[i] == three[k]:
    cache[i][j] = compare(one, two, three, i+1, j, cache)
    if cache[i][j]:
      return True
  if j < len(two) and two[j] == three[k]:
    cache[i][j] = compare(one, two, three, i, j+1, cache)
    if cache[i][j]:
      return True
  cache[i][j] = False
  return False