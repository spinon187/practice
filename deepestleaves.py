class Solution:
    def deepestLeavesSum(self, root):
        table = {}
        maxDepth = self.traverse(root, table, 0, 0)
        return sum(table[maxDepth])
        
        
    def traverse(self, node, table, depth, maxDepth):
        if not node:
            return maxDepth
        maxDepth = max(maxDepth, depth)
        if depth not in table:
            table[depth] = []
        table[depth].append(node.val)
        maxDepth = max(self.traverse(node.left, table, depth+1, maxDepth), self.traverse(node.right, table, depth+1, maxDepth))
        return maxDepth