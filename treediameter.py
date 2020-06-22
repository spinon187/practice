class Solution:
    def diameterOfBinaryTree(self, root):
        _, b = self.traverse(root)
        return b
        
        
    def traverse(self, node):
        if not node:
            return [0,0]
        leftRunning, leftMax = self.traverse(node.left)
        rightRunning, rightMax = self.traverse(node.right)
        currMax = max(leftMax, rightMax, leftRunning+rightRunning)
        running = max(leftRunning+1, rightRunning+1)
        return [running, currMax]