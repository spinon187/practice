def largestRange(array):
  vals = {}
  longest = []
  for i in array:
    vals[i] = False
  for i in array:
    if vals[i] is False:
      vals[i] = True
      temp = [i]
      x = i-1
      y = i+1
      while x in vals:
        vals[x] = True
        temp = [x] + temp
        x -= 1
      while y in vals:
        vals[y] = True
        temp.append(y)
        y += 1
      if len(temp) > len(longest):
        longest = temp
  
  return [longest[0], longest[-1]]