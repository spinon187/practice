class Solution:
    def __init__(self):
        self.memo = {}
    
    def lcaDeepestLeaves(self, root):          
        return self.traverse(root)
        
    
    def traverse(self, node):
        if not node:
            return 0
        if self.getHeight(node.left) == self.getHeight(node.right):
            return node
        elif self.getHeight(node.left) > self.getHeight(node.right):
            return self.traverse(node.left)
        else:
            return self.traverse(node.right)
        
    def getHeight(self, node):
        if node in self.memo:
            return self.memo[node]
        if not node:
            return 0
        result = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        self.memo[node] = result
        return result
                