def longestStringChain(strings):
  chains = {}
  for string in strings:
    chains[string] = {'next': '', 'max': 1}
  sortedStrings = sorted(strings, key=len)
  for string in sortedStrings:
    getLongest(string, chains)
    
  return compileLongest(strings, chains)
    
def getLongest(string, chains):
  for i in range(len(string)):
    smaller = getSmaller(string, i)
    if smaller in chains:
      compareLength(string, smaller, chains)
      
def getSmaller(string, i):
  return string[0:i] + string[i+1:]

def compareLength(curr, smaller, chains):
  smallerChain = chains[smaller]['max'] + 1
  currChain = chains[curr]['max']
  if smallerChain > currChain:
    chains[curr]['max'] = smallerChain
    chains[curr]['next'] = smaller
    
def compileLongest(strings, chains):
  maxChain = strings[0]
  for string in strings:
    if chains[string]['max'] > chains[maxChain]['max']:
      maxChain = string
      
  final = []
  curr = maxChain
  while curr != '':
    final.append(curr)
    curr = chains[curr]['next']
  
  return [] if len(final) == 1 else final