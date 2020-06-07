def rectangleMania(coords):
	table = makeTable(coords)
	return getCount(coords, table)

def makeTable(coords):
	table = {}
	for c in coords:
		tup = (c[0], c[1])
		table[tup] = True
	return table

def getCount(coords, table):
	count = 0
	for x1, y1 in coords:
		for x2, y2 in coords:
			if validUpperRight([x1, y1], [x2, y2]):
				if (x1, y2) in table and (x2, y1) in table:
					count += 1
	return count
			
def validUpperRight(c1, c2):
	x1, y1 = c1
	x2, y2 = c2
	return x2 > x1 and y2 > y1