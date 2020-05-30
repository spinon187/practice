def longestPalindromicSubstring(string):
  longest = [0, 1]
	for i in range(1, len(string)):
		odd = getPal(string, i-1, i+1)
		even = getPal(string, i-1, i)
		bigger = max(odd, even, key=lambda x: x[1] - x[0])
		longest = max(longest, bigger, key=lambda x: x[1] - x[0])
	return string[longest[0]:longest[1]]

def getPal(string, left, right):
	while left >= 0 and right < len(string):
		if string[left] != string[right]:
			break
		left -= 1
		right += 1
	return [left+1, right]