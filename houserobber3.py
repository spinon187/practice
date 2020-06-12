class Solution:
    def rob(self, root):
        return max(self.dfs(root))
    
    def dfs(self, node):
        if node is None:
            return (0, 0)
        leftVals = self.dfs(node.left)
        rightVals = self.dfs(node.right)
        doRob = node.val + leftVals[1] + rightVals[1]
        dontRob = max(leftVals[0], leftVals[1]) + max(rightVals[0], rightVals[1])
        return (doRob, dontRob)