class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        results, q = [root.val], [root]
        
        while q:
            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                results.append(next_level[-1].val)
            q = next_level
        
        return results