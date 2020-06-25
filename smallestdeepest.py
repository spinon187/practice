class Solution:
    def subtreeWithAllDeepest(self, root):
        
        def traverse(node, depth):
            if not node:
                return (depth, node)
            left_depth, left_root = traverse(node.left, depth+1)
            right_depth, right_root = traverse(node.right, depth+1)
            if left_depth > right_depth:
                return (left_depth, left_root)
            if right_depth > left_depth:
                return (right_depth, right_root)
            else:
                return (left_depth, node)
        
        return traverse(root, 0)[1]