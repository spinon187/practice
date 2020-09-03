class Solution:
    def detectCapitalUse(self, word):
        for x in range(1, len(word)):
            if word[x].isupper() and word[x-1].islower():
                return False
            elif x > 1 and word[x].islower() and word[x-1].isupper():
                return False
        return True