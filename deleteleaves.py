class Solution:
    def removeLeafNodes(self, root, target):
        return self.traverse(root, target)
    
    def traverse(self, node, target):
        if node is None:
            return None
        node.left, node.right = self.traverse(node.left, target), self.traverse(node.right, target)
        return None if node.val == target and node.left == node.right else node