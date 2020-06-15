class Solution:
    def wordBreak(self, s, wordDict):
        d = [False for _ in s]
        for c in range(len(s)):
            for word in wordDict:
                if word == s[c+1 - len(word):c+1] and (d[c - len(word)] or c-len(word) == -1):
                    d[c] = True
        return d[-1]