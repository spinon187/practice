class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q, results = [root], [[root.val]]
        while q:
            nextLevel, nextVals = [], []
            for node in q:
                if node.left:
                    nextLevel.append(node.left)
                    nextVals.append(node.left.val)
                if node.right:
                    nextLevel.append(node.right)
                    nextVals.append(node.right.val)
            if nextVals: results.append(nextVals)
            q = nextLevel
        return reversed(results)