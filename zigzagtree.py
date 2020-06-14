class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        results = []
        level = 1
        while len(queue):
            nextLevel = []
            values = []
            for node in queue:
                values.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if level % 2 != 0:
                results.append(values)
            else:
                results.append(reversed(values))
            level += 1
            queue = nextLevel
            
        return results