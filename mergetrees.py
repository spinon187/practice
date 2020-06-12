def mergeTrees(t1, t2):
    if t1 is None and t2 is None:
        return None
    t3 = TreeNode(0)
    if t1 is None:
        t3.val = t2.val
        t3.left = t2.left
        t3.right = t2.right
    elif t2 is None:
        t3.val = t1.val
        t3.left = t1.left
        t3.right = t1.right
    else:
        t3.val = t1.val + t2.val
        t3.left = mergeTrees(t1.left, t2.left)
        t3.right = mergeTrees(t1.right, t2.right)
    return t3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right