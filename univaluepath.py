class Solution:
    def longestUnivaluePath(self, root):
        return self.traverse(root)[0]
        
    def traverse(self, root):
        if not root:
            return [0, 0]
        leftMax, leftRunning = self.traverse(root.left)
        rightMax, rightRunning = self.traverse(root.right)
        leftRunning = 1 + leftRunning if root.left and root.left.val == root.val else 0
        rightRunning = 1 + rightRunning if root.right and root.right.val == root.val else 0
        return [max(leftMax, rightMax, leftRunning + rightRunning), max(leftRunning, rightRunning)]