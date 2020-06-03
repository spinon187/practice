def getLowestCommonManager(topManager, reportOne, reportTwo):
  return helper(topManager, reportOne, reportTwo)[0]

def helper(node, val1, val2):
  total = 0
  for d in node.directReports:
    results = helper(d, val1, val2)
    if results[0] is not None:
      return results
    total += results[1]
  if node == val1 or node == val2:
    total += 1
  lcm = node if total == 2 else None
  return [lcm, total]