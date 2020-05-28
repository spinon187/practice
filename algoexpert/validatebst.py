def validateBst(tree):
	return bstHelper(tree, float('-inf'), float('inf'))

	
def bstHelper(tree, minVal, maxVal):
	if tree is None:
		return True
	if tree.value < minVal or tree.value >= maxVal:
		return False
	leftValid = bstHelper(tree.left, minVal, tree.value)
	rightValid = bstHelper(tree.right, tree.value, maxVal)
	if leftValid is False or rightValid is False:
		return False
	else:
		return True