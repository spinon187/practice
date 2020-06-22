class Solution:
    def sumOfLeftLeaves(self, root, isLeft=False):
        if not root:
            return 0
        if not root.left and not root.right:
            if isLeft:
                return root.val
            else:
                return 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)