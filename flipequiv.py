class Solution:
    def flipEquiv(self, root1, root2):
        def traverse(node, table, parent = None):
            if not node:
                return table
            table[node.val] = parent
            traverse(node.left, table, node.val)
            traverse(node.right, table, node.val)
            return table
        return traverse(root1, {}) == traverse(root2, {})