def waterArea(heights):
  leftMax = [0 for x in range(len(heights))]
  rightMax = [0 for x in range(len(heights))]
  latest = 0
  for i in range(len(heights)):
    if heights[i] > latest:
      latest = heights[i]
    leftMax[i] = latest
  latest = 0
  for i in reversed(range(len(heights))):
    if heights[i] > latest:
      latest = heights[i]
    rightMax[i] = latest
  total = 0
  for i in range(len(heights)):
    toAdd = min(leftMax[i], rightMax[i]) - heights[i]
    if toAdd > 0:
      total += toAdd
  return total