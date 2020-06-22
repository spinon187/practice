class Solution:
    def findTilt(self, root):
        _, tilt = self.traverse(root)
        return tilt
        
        
    def traverse(self, root):
        if not root:
            return [0, 0]
        leftSum, leftTilt = self.traverse(root.left)
        rightSum, rightTilt = self.traverse(root.right)
        return [root.val + leftSum + rightSum, leftTilt+rightTilt+abs(leftSum - rightSum)]