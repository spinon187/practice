class Solution:
    def __init__(self):
        self.moves = 0
    
    def distributeCoins(self, root):
        self.calculate(root)
        return self.moves
    
    def calculate(self, node):
        if not node:
            return 0
        left = self.calculate(node.left)
        balance = node.val - 1
        right = self.calculate(node.right)
        self.moves += abs(left) + abs(right)
        return left + balance + right