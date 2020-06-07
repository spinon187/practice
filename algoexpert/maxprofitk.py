def maxProfitWithKTransactions(prices, k):
  if len(prices) < 2:
    return 0
  prev = [0 for p in prices]
  curr = prev[:]
  for x in range(k):
    runningmax = float('-inf')
    for p in range(1, len(prices)):
      runningmax = max(runningmax, prev[p-1] - prices[p - 1])
      curr[p] = max(curr[p-1], runningmax + prices[p])
    prev = curr[:]
  return curr[-1]