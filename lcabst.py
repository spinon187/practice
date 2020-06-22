class Solution:
    def lowestCommonAncestor(self, root, p, q):
        _, result = self.traverse(root, p.val, q.val, 0)
        return result
        
        
    def traverse(self, node, p, q, count):
        if not node:
            return [count, None]
        leftCount, rightCount, leftLCA, rightLCA = 0, 0, None, None
        if node.val > p or node.val > q:
            leftCount, leftLCA = self.traverse(node.left, p, q, count)
        if node.val <= p or node.val <= q:
            rightCount, rightLCA = self.traverse(node.right, p, q, count)
        LCA = leftLCA or rightLCA
        count = leftCount + rightCount
        if node.val == p or node.val == q:
            count += 1
        if count == 2 and LCA is None:
            LCA = node
        return [count, LCA]