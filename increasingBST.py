class Solution:
    def increasingBST(self, root):
        order, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            order.append(node)
            root = node.right
        for n in range(len(order)-1):
            node = order[n]
            node.left = None
            node.right = order[n+1]
        return order[0]