class Solution:
    def minDistance(self, word1, word2):
        small = word1 if word1 < word2 else word2
        big = word1 if word1 >= word2 else word2
        comparisons = [x for x in range(len(small) + 1)]
        current = [0]
        for row in range(1, len(big) + 1):
            if row > 1:
                comparisons = current
            current = [row]
            for col in range(1, len(small) + 1):
                if big[row-1] == small[col-1]:
                    current.append(comparisons[col-1])
                else:
                    current.append(1 + min(current[col-1], comparisons[col-1], comparisons[col]))
        return current[-1]