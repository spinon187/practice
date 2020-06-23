class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q, results = [root], [[root.val]]
        while q:
            next_level = []
            vals = []
            for node in q:
                for child in node.children:
                    next_level.append(child)
                    vals.append(child.val)
            if vals: results.append(vals)
            q = next_level
        return results