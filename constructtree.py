class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        j = 0
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            parent = stack[-1]
            isLeft = True
            node = TreeNode(i)
            
            while stack and inorder[j] == stack[-1].val:
                parent = stack.pop()
                isLeft = False
                j += 1
                
            if isLeft:
                parent.left = node
            else:
                parent.right = node
                
            stack.append(node)
            
        return root