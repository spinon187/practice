def apartmentHunting(blocks, reqs):
	table = {}
	flattened = [float('-inf')]*len(blocks)
	for r in reqs:
		table[r] = [None for b in blocks]
		getLocalMin(blocks, table, r)
		for i, block in enumerate(table[r]):
			flattened[i] = max(flattened[i], block)
	low = 0
	for i in flattened:
		if flattened[low] > flattened[i]:
			low = i
	return low

def getLocalMin(blocks, table, key):
	nearest = None
	for i in range(len(blocks)):
		if blocks[i][key] == True:
			nearest = 0
			table[key][i] = 0
		elif nearest is not None:
			nearest += 1
			table[key][i] = nearest
	nearest = None
	for i in reversed(range(len(blocks))):
		if blocks[i][key] == True:
			nearest = 0
		elif nearest is not None:
			nearest += 1
			table[key][i] = min(table[key][i], nearest) if table[key][i] is not None else nearest