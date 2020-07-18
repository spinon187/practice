from collections import deque

class Solution:
    def isCompleteTree(self, root):
        deq = deque([root])
        while deq:
            node = deq.popleft()
            if not node:
                break
            deq.extend([node.left, node.right])
        return not any(deq)