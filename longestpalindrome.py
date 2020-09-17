class Solution:
    def longestPalindrome(self, s):
        seen = set()
        max_len = 0
        for letter in s:
            if letter in seen:
                seen.remove(letter)
                max_len += 2
            else:
                seen.add(letter)
        return max_len + 1 if len(seen) else max_len