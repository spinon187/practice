class Solution:
    def convertBST(self, root):
        stack, total = [], 0
        ret = root
        while root or stack:
            while(root):
                stack.append(root)
                root = root.right
            node = stack.pop()
            total += node.val
            node.val = total
            root = node.left
        return ret