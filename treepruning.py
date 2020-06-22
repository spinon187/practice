class Solution:
    def pruneTree(self, root):
        self.traverse(root)
        return root
        
        
    def traverse(self, node):
        if not node:
            return False
        leftCheck, rightCheck = self.traverse(node.left), self.traverse(node.right)
        if leftCheck is False:
            node.left = None
        if rightCheck is False:
            node.right = None
        if node.val == 1 or leftCheck or rightCheck:
            return True
        else:
            return False