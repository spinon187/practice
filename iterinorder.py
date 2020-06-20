class Solution:
    def inorderTraversal(self, root):
        results, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return results
            node = stack.pop()
            results.append(node.val)
            root = node.right