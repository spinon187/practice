def underscorifySubstring(string, substring):
  pointer = 0
  raw = []
  while pointer < len(string):
    i = string.find(substring, pointer)
    if i == -1:
      if not len(raw):
        return string
      else:
        break
    else:
      raw.append([i, i+len(substring)])
      pointer = i+1

  refined = [[raw[0][0], raw[0][1]]]
  for x in range(1, len(raw)):
    if raw[x][0] <= refined[-1][1]:
      refined[-1][1] = raw[x][1]
    else:
      refined.append(raw[x])
    
  adjuster = 0
  final = list(string)
  for x in range(len(refined)):
    final.insert(refined[x][0]+adjuster, '_')
    final.insert(refined[x][1]+1+adjuster, '_')
    adjuster += 2
  return ''.join(final)