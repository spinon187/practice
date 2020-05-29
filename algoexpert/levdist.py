def levenshteinDistance(str1, str2):
  small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	comps = [x for x in range(len(small) + 1)]
	curr = [0]
	for row in range(1, len(big)+1):
		if(row > 1):
			comps = curr
		curr = [row]
		for col in range(1, len(small)+1):
			if big[row-1] == small[col-1]:
				curr.append(comps[col-1])
			else:
				curr.append(1 + min(curr[col-1], comps[col], comps[col-1]))
	return curr[-1]