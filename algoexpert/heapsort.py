def heapSort(array):
  heapify(array)
  for i in reversed(range(1, len(array))):
    swap(0, i, array)
    siftDown(0, i-1, array)
  return array

def heapify(array):
  firstParent = (len(array) - 2) // 2
  for x in reversed(range(firstParent + 1)):
    siftDown(x, len(array)-1, array)
    
def siftDown(i, end, heap):
  left = i*2+1
  while left <= end:
    right = i*2+2 if i*2+2 <= end else -1
    if right > -1 and heap[right] > heap[left]:
      target = right
    else:
      target = left
    if heap[target] > heap[i]:
      swap(i, target, heap)
      i = target
      left = i*2+1
    else:
      return
      
def swap(i, j, array):
  array[i], array[j] = array[j], array[i]