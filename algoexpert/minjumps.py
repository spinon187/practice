# def minNumberOfJumps(array):
#   minJumps = [float('inf') for x in range(len(array))]
# 	minJumps[0] = 0
# 	for i in range(len(array)-1):
# 		for j in range(1, array[i]+1):
# 			if i+j < len(array):
# 				minJumps[i+j] = min(minJumps[i]+1, minJumps[i+j])
# 	return minJumps[-1]

def minNumberOfJumps(array):
  if len(array) == 1:
    return 0
  maxReach = array[0]
  jumps = 0
  steps = array[0]
  for i in range(1, len(array)-1):
    maxReach = max(maxReach, i+array[i])
    steps -= 1
    if steps == 0:
      jumps += 1
      steps = maxReach - i
  return jumps + 1