class Solution:
    def insertIntoMaxTree(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root