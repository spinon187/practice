# class Solution:
#     def deepestLeavesSum(self, root):
#         table = {}
#         maxDepth = self.traverse(root, table, 0, 0)
#         return sum(table[maxDepth])
        
        
#     def traverse(self, node, table, depth, maxDepth):
#         if not node:
#             return maxDepth
#         maxDepth = max(maxDepth, depth)
#         if depth not in table:
#             table[depth] = []
#         table[depth].append(node.val)
#         maxDepth = max(self.traverse(node.left, table, depth+1, maxDepth), self.traverse(node.right, table, depth+1, maxDepth))
#         return maxDepth

class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0
        q = [root]
        while q:
            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(next_level):
                q = next_level
            else:
                vals = []
                for node in q:
                    vals.append(node.val)
                return sum(vals)