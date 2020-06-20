class Solution:
    def tree2str(self, t):
        if t is None:
            return ''
        if t.left is None and t.right is None:
            return str(t.val)
        
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        
        if not right:
            return str(t.val) + '('+left+')'
        else:
            return str(t.val) + '('+left+')' + '('+right+')'