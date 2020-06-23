class Solution:
    def goodNodes(self, root, prev=float('-inf')):
        if not root:
            return 0
        prev = max(prev, root.val)
        count = self.goodNodes(root.left, prev) + self.goodNodes(root.right, prev)
        return count + 1 if root.val >= prev else count