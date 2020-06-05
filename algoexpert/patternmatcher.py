def patternMatcher(pattern, string):
	if len(pattern) > len(string):
		return []
	p = xFirst(pattern)
	flipped = p[0] != pattern[0]
	counts = {'x':0, 'y':0}
	firstY = countsAndIndex(p, counts)
	if counts['y'] > 0:
		for lenX in range(1, len(string)):
			lenY = (len(string) - lenX * counts['x']) / counts['y']
			if lenY > 0 and lenY % 1 == 0:
				lenY = int(lenY)
				yIndex = firstY * lenX
				x = string[:lenX]
				y = string[yIndex : yIndex + lenY]
				comp = map(lambda char: x if char == 'x' else y, p)
				if string == ''.join(comp):
					return [x, y] if not flipped else [y, x]
	else:
		lenX = len(string) / counts['x']
		if lenX % 1 == 0:
			lenX = int(lenX)
			x = string[:lenX]
			comp = map(lambda char: x, p)
			if string == ''.join(comp):
				return [x, ''] if not flipped else ['', x]
	return []



def countsAndIndex(pattern, counts):
	y = None
	for i, char in enumerate(pattern):
		counts[char] += 1
		if char == 'y' and y == None:
			y = i
	return y


def xFirst(pattern):
	arr = list(pattern)
	if arr[0] == 'x':
		return arr
	else:
		return list(map(lambda char: 'x' if char == 'y' else 'y', arr))