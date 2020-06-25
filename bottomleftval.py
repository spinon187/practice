class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None
        q = [root]
        while q:
            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if not next_level:
                return q[0].val
            else:
                q = next_level