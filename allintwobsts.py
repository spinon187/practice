class Solution:
    def getAllElements(self, root1, root2):
        left, right = [], []
        self.traverse(root1, left)
        self.traverse(root2, right)
        return sorted(left + right)
        
        
    def traverse(self, node, arr):
        if not node:
            return
        arr.append(node.val)
        self.traverse(node.left, arr)
        self.traverse(node.right, arr)

# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         results, stack1, stack2 = [], [], []
#         while (stack1 or root1) and (stack2 or root2):
#             while root1:
#                 stack1.append(root1)
#                 root1 = root1.left
#             while root2:
#                 stack2.append(root2)
#                 root2 = root2.left
                    
#             if stack1[-1].val < stack2[-1].val:
#                 node = stack1.pop()
#                 root1 = node.right
#             else:
#                 node = stack2.pop()
#                 root2 = node.right
                
#             results.append(node.val)
            
#         if not stack1 or not stack2:
#             stack3, root3 = stack1 or stack2, root1 or root2
#             while root3 or stack3:
#                 while root3:
#                     stack3.append(root3)
#                     root3 = root3.left
#                 node = stack3.pop()
#                 root3 = node.right
#                 results.append(node.val)
                
#         return results