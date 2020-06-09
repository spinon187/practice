def rightSmallerThan(array):
  if len(array) == 0:
    return []
  
  output = array[:]
  last = len(array) - 1
  bst = ModifiedBST(array[last])
  output[last] = 0
  for i in reversed(range(len(array) - 1)):
    bst.insert(array[i], i, output)
    
  return output


class ModifiedBST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.leftSize = 0
    
  def insert(self, value, index, output, lessThan=0):
    if value < self.value:
      self.leftSize += 1
      if self.left is None:
        self.left = ModifiedBST(value)
        output[index] = lessThan
      else:
        self.left.insert(value, index, output, lessThan)
    else:
      lessThan += self.leftSize
      if value > self.value:
        lessThan += 1
      if self.right is None:
        self.right = ModifiedBST(value)
        output[index] = lessThan
      else:
        self.right.insert(value, index, output, lessThan)