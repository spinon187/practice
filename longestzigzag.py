class Solution:
    def longestZigZag(self, root):
        
        def traverse(node, left_sum, right_sum):
            if node.left:
                next_left = traverse(node.left, right_sum + 1, 0)
            else:
                next_left = right_sum
            if node.right:
                next_right = traverse(node.right, 0, left_sum + 1)
            else:
                next_right = left_sum
            return max(next_left, next_right)
            
        
        return traverse(root, 0, 0)