class Solution:
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        leftIsValid = self.isValidBST(root.left, floor, root.val)
        rightIsValid = self.isValidBST(root.right, root.val, ceiling)
        return leftIsValid and rightIsValid