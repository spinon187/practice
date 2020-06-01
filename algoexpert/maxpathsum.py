def maxPathSum(tree):
	_, maxSum = helper(tree)
	return maxSum
	
	
def helper(tree):
	if tree is None:
		return (0, float('-inf'))
	left, leftMax = helper(tree.left)
	right, rightMax = helper(tree.right)
	maxChildBranch = max(left, right)
	val = tree.value
	maxAsBranch = max(maxChildBranch + val, val)
	maxAsRoot = max(left + right + val, maxAsBranch)
	maxSum = max(leftMax, rightMax, maxAsRoot)
	
	return (maxAsBranch, maxSum)