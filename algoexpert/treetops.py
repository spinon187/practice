def numberOfBinaryTreeTopologies(n, cache={0: 1}):
  if n in cache:
    return cache[n]
  count = 0
  for leftTree in range(n):
    rightTree = n - 1 - leftTree
    leftTreeCount = numberOfBinaryTreeTopologies(leftTree, cache)
    rightTreeCount = numberOfBinaryTreeTopologies(rightTree, cache)
    count += leftTreeCount * rightTreeCount
  cache[n] = count
  return count