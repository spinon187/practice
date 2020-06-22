class Solution:
    def pathSum(self, root, k):
        
        def traverse(node, table, running):
            if not node:
                return 0
            running += node.val
            path = table[running - k] if running-k in table else 0
            table[running] = table[running]+1 if running in table else 1
            path += traverse(node.left, table, running) + traverse(node.right, table, running)
            table[running] -= 1
            
            return path
        
        return traverse(root, {0: 1}, 0)