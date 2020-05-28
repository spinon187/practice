def invertBinaryTree(tree):
	if tree is not None:
		dummy = tree.left
		tree.left = invertBinaryTree(tree.right)
		tree.right = invertBinaryTree(dummy)
	return tree