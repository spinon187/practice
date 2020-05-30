def groupAnagrams(words):
  k = {}
	for x in words:
		raw = ''.join(sorted(x))
		if raw in k:
			k[raw].append(x)
		else:
			k[raw] = [x]
	return list(k.values())