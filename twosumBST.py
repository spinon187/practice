class Solution:
    def findTarget(self, root, k):
        seen = set()
        return self.dfs(root, seen, k)
        
    def dfs(self, node, seen, k):
        if not node:
            return False
        
        diff = k - node.val
        if diff in seen:
            return True
        else:
            seen.add(node.val)
            return self.dfs(node.left, seen, k) or self.dfs(node.right, seen, k)