class Solution:
    def findSecondMinimumValue(self, root):
        mins = [float('inf'), float('inf')]
        self.traverse(root, mins)
        if mins[0] == mins[1] or mins[1] == float('inf'):
            return -1
        else:
            return mins[1]
        
    def traverse(self, node, mins):
        if not node:
            return
        if node.val < mins[0]:
            mins[0], mins[1] = node.val, mins[0]
        elif node.val < mins[1] and node.val != mins[0]:
            mins[1] = node.val
        self.traverse(node.left, mins)
        self.traverse(node.right, mins)