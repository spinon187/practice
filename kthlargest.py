class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.minHeap = Heap(self.nums[:], k)

    def add(self, val):
        self.minHeap.insert(val)
        self.nums.append(val)
        return self.minHeap.peek()
        

class Heap:
    def __init__(self, array, maxSize):
        self.max = maxSize
        self.size = 0
        self.heap = self.heapify(array)
        
    
    def heapify(self, array):
        firstParent = (len(array) - 2) // 2
        for current in reversed(range(firstParent + 1)):
            self.siftDown(current, len(array) - 1, array)
        self.size = len(array)
        for _ in range(self.size - self.max):
            # print(_)
            self.remove(array)
            self.size -= 1
        return array
        
    def siftUp(self, current, heap):
        parent = (current - 1) // 2
        while current > 0 and heap[current] < heap[parent]:
            self.swap(current, parent, heap)
            current = parent
            parent = (current - 1) // 2
            
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
    
    def peek(self):
        return self.heap[0] if len(self.heap) else float('-inf')
    
    def insert(self, value):
        if value > self.peek() or self.size < self.max:
            if self.size >= self.max:
                self.remove(self.heap)
            else:
                self.size += 1
            self.heap.append(value)
            self.siftUp(len(self.heap) - 1, self.heap)

        
    def remove(self, heap):
        self.swap(0, len(heap) -1, heap)
        popped = heap.pop()
        self.siftDown(0, len(heap) - 1, heap)
        return popped
            
    def swap(self, node1, node2, heap):
        heap[node1], heap[node2] = heap[node2], heap[node1]