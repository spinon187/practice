class Solution:
    def findLongestChain(self, pairs):
        current, length = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if current < pair[0]:
                current = pair[1]
                length += 1
        return length