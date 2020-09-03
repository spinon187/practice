class Solution:
    def canConstruct(self, ransomNote, magazine):
        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1
        for letter in ransomNote:
            if letters[letter] > 0:
                letters[letter] -= 1
            else:
                return False
        return True