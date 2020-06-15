class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        mem = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i+1:]
                if key not in mem:
                    mem[key] = []
                mem[key].append(word)
        visited = set()
        visited.add(beginWord)
        front = [beginWord]
        length = 1
        while front:
            q = []
            for word in front:
                neighbors = []
                for i in range(len(word)):
                    key = word[:i] + '_' + word[i+1:]
                    if key in mem:
                        neighbors += mem[key]
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return length + 1
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            length += 1
            front = q
        return 0