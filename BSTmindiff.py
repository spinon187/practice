# class Solution:
#     def getMinimumDifference(self, root):
#         stack, vals, mindiff = [], [], float('inf')
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             node = stack.pop()
#             vals.append(node.val)
#             root = node.right
#         vals.sort()
#         for i in range(1, len(vals)):
#             mindiff = min(mindiff, abs(vals[i] - vals[i-1]))
#         return mindiff

class Solution:
    def getMinimumDifference(self, root):
        self.mindiff = self.prev = float('inf')
        self.traverse(root)
        
        return self.mindiff
        
    def traverse(self, node):
        if node:
            self.traverse(node.left)
            self.mindiff = min(self.mindiff, abs(self.prev - node.val))
            self.prev = node.val
            self.traverse(node.right)