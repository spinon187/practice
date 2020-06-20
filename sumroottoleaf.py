class Solution:
    def sumRootToLeaf(self, root):
        return self.recurse(root)
        
    def recurse(self, node, val=''):
        if not node:
            return 0
        val += str(node.val)
        if node.left or node.right:
            total = 0
            total += self.recurse(node.left, val)
            total += self.recurse(node.right, val)
        else:
            total = int(val, 2)
        return total