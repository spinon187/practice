# This is an input class. Do not edit.
class AncestralTree:
  def __init__(self, name):
    self.name = name
    self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	if topAncestor == descendantOne or topAncestor == descendantTwo:
		return topAncestor
  depthOne = getDepth(descendantOne, topAncestor)
	depthTwo = getDepth(descendantTwo, topAncestor)
	return traverseUp(descendantOne, descendantTwo, depthOne, depthTwo)
	
def getDepth(node, ancestor):
	depth = 1
	if node.ancestor != ancestor:
		depth += getDepth(node.ancestor, ancestor)
	return depth

def traverseUp(node1, node2, depth1=0, depth2=0):
	if node1 == node2:
		return node1
	elif depth1 == depth2:
		return traverseUp(node1.ancestor, node2.ancestor)
	elif depth1 > depth2:
		return traverseUp(node1.ancestor, node2, depth1-1, depth2)
	elif depth2 > depth1:
		return traverseUp(node1, node2.ancestor, depth1, depth2-1)