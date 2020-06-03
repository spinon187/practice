class ContinuousMedianHandler:
    def __init__(self):
      self.median = None
    self.smallHalf = Heap(MAX_HEAP, [])
    self.bigHalf = Heap(MIN_HEAP, [])

    def insert(self, number):
    if not self.smallHalf.length or number < self.smallHalf.peek():
      self.smallHalf.insert(number)
    else:
      self.bigHalf.insert(number)
    self.rebalance()
    self.updateMedian()

    def getMedian(self):
        return self.median

  def rebalance(self):
    if self.smallHalf.length - self.bigHalf.length > 1:
      self.bigHalf.insert(self.smallHalf.remove())
    elif self.bigHalf.length - self.smallHalf.length > 1:
      self.smallHalf.insert(self.bigHalf.remove())
      
  def updateMedian(self):
    if self.smallHalf.length == self.bigHalf.length:
      self.median = (self.smallHalf.peek() + self.bigHalf.peek()) / 2
    elif self.smallHalf.length > self.bigHalf.length:
      self.median = self.smallHalf.peek()
    else:
      self.median = self.bigHalf.peek()




  class Heap:
  def __init__(self, comp, array):
    self.heap = self.buildHeap(array)
    self.comp = comp
    self.length = len(self.heap)
    
  def buildHeap(self, array):
    firstParent = (len(array) - 2) // 2
    for i in reversed(range(firstParent + 1)):
      self.siftDown(i, len(array) - 1, array)
    return array

  def siftDown(self, curr, end, heap):
    childOne = curr * 2 + 1
    while childOne <= end:
      childTwo = curr * 2 + 2 if curr * 2 + 2 <= end else -1
      if childTwo != -1:
        if self.comp(heap[childTwo], heap[childOne]):
          toSwap = childTwo
        else:
          toSwap = childOne
      else:
        toSwap = childOne
      if self.comp(heap[toSwap], heap[curr]):
        self.swap(curr, toSwap, heap)
        curr = toSwap
        childOne = curr * 2 + 1
      else:
        return
      
  def siftUp(self, curr, heap):
    parent = (curr-1)//2
    while curr > 0:
      if self.comp(heap[curr], heap[parent]):
        self.swap(curr, parent, heap)
        curr = parent
        parent = (curr-1)//2
      else:
        return
      
  def peek(self):
    return self.heap[0]

  def remove(self):
    self.swap(0, self.length-1, self.heap)
    val = self.heap.pop()
    self.length -= 1
    self.siftDown(0, self.length - 1, self.heap)
    return val

  def insert(self, val):
    self.heap.append(val)
    self.length += 1
    self.siftUp(self.length - 1, self.heap)
    
  def swap(self, i, j, array):
    array[i], array[j] = array[j], array[i]
    
  def MAX_HEAP(a, b):
  return a > b

  def MIN_HEAP(a, b):
  return a < b