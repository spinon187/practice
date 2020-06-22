class Solution:
    def sumEvenGrandparent(self, node, parent=1, grandparent=1, running=0):
        if not node:
            return 0
        running = self.sumEvenGrandparent(node.left, node.val, parent, running) + self.sumEvenGrandparent(node.right, node.val, parent, running)
        if not grandparent % 2:
            running += node.val
        return running