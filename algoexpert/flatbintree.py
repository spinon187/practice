# This is the class of the input root. Do not edit it.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def flattenBinaryTree(tree):
	leftMost, _ = traverse(tree)
	return leftMost
	
def traverse(node):
  if node.left is None:
    leftMost = node
  else:
    leftLM, leftRM = traverse(node.left)
    updatePointers(leftRM, node)
    leftMost = leftLM
  if node.right is None:
    rightMost = node
  else:
    rightLM, rightRM = traverse(node.right)
    updatePointers(node, rightLM)
    rightMost = rightRM
  return [leftMost, rightMost]

def updatePointers(left, right):
  left.right = right
  right.left = left