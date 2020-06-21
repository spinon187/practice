class Solution:
    def binaryTreePaths(self, root):
        results = []
        self.dfs(root, '', results)
        return results
        
    def dfs(self, node, string, arr):
        if not node:
            return
        if node.left or node.right:
            string += (str(node.val) + '->')
            self.dfs(node.left, string, arr)
            self.dfs(node.right, string, arr)
        else:
            string += str(node.val)
            arr.append(string)