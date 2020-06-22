class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            root = TreeNode(val)
        else:
            self.traverseBST(root, val)
        return root
        
        
    def traverseBST(self, root, val):
        if val > root.val:
            if root.right:
                self.traverseBST(root.right, val)
            else:
                root.right = TreeNode(val)
        if val < root.val:
            if root.left:
                self.traverseBST(root.left, val)
            else:
                root.left = TreeNode(val)