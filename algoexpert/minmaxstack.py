# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.minMax = []
		
  def peek(self):
    return self.stack[-1]

  def pop(self):
    self.minMax.pop()
    return self.stack.pop()

  def push(self, number):
    self.stack.append(number)
    if len(self.minMax) == 0:
      self.minMax.append([number, number])
    elif self.minMax[-1][0] > number:
      self.minMax.append([number, self.minMax[-1][1]])
    elif self.minMax[-1][1] < number:
      self.minMax.append([self.minMax[-1][0], number])
    else:
      self.minMax.append(self.minMax[-1])
    
  def getMin(self):
    return self.minMax[-1][0]

  def getMax(self):
    return self.minMax[-1][1]