def knapsackProblem(items, capacity):
  combos = [[0 for x in range(capacity+1)] for y in range(len(items)+1)]
  for row in range(1, len(combos)):
    weight = items[row-1][1]
    value = items[row-1][0]
    for col in range(0, len(combos[0])):
      if weight <= col:
        extra = combos[row-1][col - weight]
        combos[row][col] = max(combos[row-1][col], value + extra)
      else:
        combos[row][col] = combos[row-1][col]


  return [combos[-1][-1], getItems(combos, items)]

def getItems(combos, items):
  seq = []
  row = len(combos)-1
  col = len(combos[0])-1
  while row > 0:
    if combos[row][col] == combos[row-1][col]:
      row -= 1
    else:
      seq = [row-1] + seq
      col -= items[row-1][1]
      row -= 1
    if col == 0:
      break
  return seq