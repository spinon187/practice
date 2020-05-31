def minRewards(scores):
  treats = [1]*len(scores)
  for i in range(0, len(scores)-1):
    if scores[i] < scores[i+1]:
      treats[i+1] = treats[i] + 1
  for i in reversed(range(len(scores)-1)):
    if scores[i] > scores[i+1]:
      treats[i] = max(treats[i], treats[i+1]+1)
  return sum(treats)