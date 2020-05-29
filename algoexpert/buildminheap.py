# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
  def __init__(self, array):
    # Do not edit the line below.
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    firstParent = (len(array) -2) // 2
		for current in reversed(range(firstParent + 1)):
			self.siftDown(current, len(array) - 1, array)
		return array

  def siftDown(self, current, end, heap):
    childOne = current * 2 + 1
		while childOne <= end:
			childTwo = current * 2 + 2 if current * 2 + 2 <= end else -1
			if childTwo != -1 and heap[childTwo] < heap[childOne]:
				toSwap = childTwo
			else:
				toSwap = childOne
			if heap[toSwap] < heap[current]:
				self.swap(current, toSwap, heap)
				current = toSwap
				childOne = current * 2 + 1
			else:
				return

  def siftUp(self, current, heap):
    parent = (current - 1) // 2
		while current > 0 and heap[current] < heap[parent]:
			self.swap(current, parent, heap)
			current = parent
			parent = (current - 1) // 2

  def peek(self):
    return self.heap[0]
	
	def getLast(self):
		return len(self.heap) - 1

  def remove(self):
    self.swap(0, self.getLast(), self.heap)
		popped = self.heap.pop()
		self.siftDown(0, self.getLast(), self.heap)
		return popped

  def insert(self, value):
    self.heap.append(value)
		self.siftUp(self.getLast(), self.heap)

	def swap(self, node1, node2, heap):
		heap[node1], heap[node2] = heap[node2], heap[node1]