def boggleBoard(board, words):
  trie = Trie()
  for w in words:
    trie.add(w)
  output = {}
  visited = [[False for col in row] for row in board]
  for i in range(len(board)):
    for j in range(len(board[i])):
      traverse(board, i, j, trie.root, visited, output)
  return list(output.keys())



  def traverse(board, row, col, trie, visited, output):
  if visited[row][col]:
    return
  char = board[row][col]
  if char not in trie:
    return
  visited[row][col] = True
  trie = trie[char]
  if '*' in trie:
    output[trie['*']] = True
  neighbors = getNeighbors(board, row, col)
  for n in neighbors:
    traverse(board, n[0], n[1], trie, visited, output)
  visited[row][col] = False

  def getNeighbors(board, row, col):
  neighbors = []
  if row > 0:
    neighbors.append([row-1, col])
    if col > 0:
      neighbors.append([row-1, col-1])
    if col < len(board[0])-1:
      neighbors.append([row-1, col+1])
  if col > 0:
    neighbors.append([row, col-1])
  if col < len(board[0])-1:
    neighbors.append([row, col+1])
  if row < len(board)-1:
    neighbors.append([row+1, col])
    if col > 0:
      neighbors.append([row+1, col-1])
    if col < len(board[0])-1:
      neighbors.append([row+1, col+1])
  return neighbors

  class Trie:
  def __init__(self):
    self.root = {}
    self.end = '*'
  def add(self, word):
    curr = self.root
    for char in word:
      if char not in curr:
        curr[char] = {}
      curr = curr[char]
    curr[self.end] = word