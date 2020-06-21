class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, results = [(root, False)], []
        while stack:
            node, shouldAdd = stack.pop()
            if not shouldAdd:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                results.append(node.val)
        return results