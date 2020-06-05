def longestSubstringWithoutDuplication(string):
  d = {}
  longest = [0,0]
  pointer = 0
  for i in range(len(string)):
    l = string[i]
    if l not in d:
      d[l] = i
    else:
      pointer = max(pointer, d[l]+1)
      d[l] = i
    diff = i - pointer + 1
    if diff > longest[1] - longest[0] + 1:
      longest = [pointer, i]

  return string[longest[0]:longest[1]+1]