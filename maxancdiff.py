class Solution:
    def maxAncestorDiff(self, root):
        
        def traverse(node, maxVal, minVal):
            if node is None:
                return 0
            return max(
                abs(maxVal - node.val),
                abs(minVal - node.val),
                traverse(node.left, max(maxVal, node.val), min(minVal, node.val)),
                traverse(node.right, max(maxVal, node.val), min(minVal, node.val))
            )
        
        return traverse(root, root.val, root.val)