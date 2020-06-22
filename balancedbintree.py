class Solution:
    def isBalanced(self, root):
        return self.traverse(root) != -1
        
    def traverse(self, node):
        if node is None:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return 1 + max(left, right)