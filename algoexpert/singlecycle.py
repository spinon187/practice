def hasSingleCycle(array, start=0):
  jumped = 0
	curr = start
	while jumped < len(array):
		if jumped > 0 and curr == start:
			return False
		jumped += 1
		curr = getNext(curr, array)
	return curr == start

def getNext(curr, array):
	distance = array[curr]
	target = (curr + distance) % len(array)
	return target if target >=0 else target + len(array)