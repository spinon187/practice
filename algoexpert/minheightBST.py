def minHeightBst(array):
  return findLR(array, 0, len(array)-1)

def findLR(array, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	node = BST(array[mid])
	node.left = findLR(array, start, mid-1)
	node.right = findLR(array, mid+1, end)
	return node
