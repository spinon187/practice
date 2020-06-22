class Solution:
    def isSubtree(self, s, t):
        return self.stringify(t) in self.stringify(s)
        
    def stringify(self, root):
        if not root:
            return None
        return f'/{root.val} {self.stringify(root.left)} {self.stringify(root.right)}'