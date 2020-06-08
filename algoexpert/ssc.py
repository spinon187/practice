def smallestSubstringContaining(bigString, smallString):
	targets = getCounts(smallString)
	smallest = getSmallest(bigString, targets) 
	j, i = smallest
	return bigString[j:i+1] if i != float('inf') else ''
	
	
def getSmallest(string, targets):
	smallest = [0, float('inf')]
	subcounts = {}
	targetNum = len(targets.keys())
	towardTarget = 0
	i = 0
	j = 0
	while i < len(string):
		right = string[i]
		if right not in targets:
			i += 1
			continue
		increaseCount(right, subcounts)
		if subcounts[right] == targets[right]:
			towardTarget += 1
		while towardTarget == targetNum and j <= i:
			smallest = compare(j, i, smallest[0], smallest[1])
			left = string[j]
			if left not in targets:
				j += 1
				continue
			if subcounts[left] == targets[left]:
				towardTarget -= 1
			decreaseCount(left, subcounts)
			j += 1
		i += 1
	return smallest
			

def compare(left, right, oldLeft, oldRight):
	return [left, right] if right - left < oldRight - oldLeft else [oldLeft, oldRight]
	
def getCounts(string):
	counts = {}
	for c in string:
		increaseCount(c, counts)
	return counts

def increaseCount(c, counts):
	if c not in counts:
		counts[c] = 0
	counts[c] += 1
	
def decreaseCount(c, counts):
	counts[c] -= 1