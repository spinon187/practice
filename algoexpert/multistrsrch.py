def multiStringSearch(bigString, smallStrings):
  trie = Trie()
  for string in smallStrings:
    trie.insert(string)
  targets = {}
  for i in range(len(bigString)):
    traverseTrie(bigString, i, trie, targets)
  return [x in targets for x in smallStrings]


  def traverseTrie(string, i, trie, targets):
  node = trie.root
  for i in range(i, len(string)):
    char = string[i]
    if char not in node:
      break
    node = node[char]
    if trie.endSymbol in node:
      targets[node[trie.endSymbol]] = True

  class Trie:
  def __init__(self):
    self.root = {}
    self.endSymbol = '*'
    
  def insert(self, string):
    curr = self.root
    for i in range(len(string)):
      if string[i] not in curr:
        curr[string[i]] = {}
      curr = curr[string[i]]
    curr[self.endSymbol] = string