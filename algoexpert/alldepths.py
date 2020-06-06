def allKindsOfNodeDepths(root):
	return traverse(root)[2]
	
def traverse(node):
	if node is None:
		return (0, 0, 0)
	leftTree = traverse(node.left)
	rightTree = traverse(node.right)
	
	sumLeft = leftTree[0] + leftTree[1]
	sumRight = rightTree[0] + rightTree[1]
	
	numNodes = 1 + leftTree[1] + rightTree[1]
	sumTree = sumLeft + sumRight
	totalSum = sumTree + leftTree[2] + rightTree[2]
	
	return (sumTree, numNodes, totalSum)

# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None