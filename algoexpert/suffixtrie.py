class SuffixTrie:
  def __init__(self, string):
    self.root = {}
    self.endSymbol = "*"
    self.populateSuffixTrieFrom(string)

  def populateSuffixTrieFrom(self, string):
    for x in range(len(string)):
			self.insert(x, string)
	
	def insert(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True

    def contains(self, string):
      node = self.root
      for c in string:
        if c not in node:
          return False
        node = node[c]
      return self.endSymbol in node