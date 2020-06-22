class Solution:
    def getAllElements(self, root1, root2):
        left, right = [], []
        self.traverse(root1, left)
        self.traverse(root2, right)
        return sorted(left + right)
        
        
    def traverse(self, node, arr):
        if not node:
            return
        arr.append(node.val)
        self.traverse(node.left, arr)
        self.traverse(node.right, arr)