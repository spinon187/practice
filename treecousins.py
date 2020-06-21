class Solution:
    def isCousins(self, root, x, y):
        q = [root]
        pair = []
        
        while q:
            nextLevel = []
            for node in q:
                if node.left:
                    if node.left.val == x or node.left.val == y:
                        pair.append(node.val)
                    nextLevel.append(node.left)
                if node.right:
                    if node.right.val == x or node.right.val == y:
                        pair.append(node.val)
                    nextLevel.append(node.right)
            if len(pair) == 1:
                return False
            elif len(pair) == 2:
                return pair[0] != pair[1]
            q = nextLevel
        return False