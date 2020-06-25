class Solution:
    def kthSmallest(self, root, k):
        stack, count = [], 0
        while count < k:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            count += 1
            root = curr.right
        return curr.val