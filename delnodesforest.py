class Solution:
    def __init__(self):
        self.results = []
    
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        self.traverse(root, to_delete_set)
        return self.results

    def traverse(self, root, to_delete, parent=None, isLeft=True):
        if not root:
            return
        if root.val in to_delete:
            if parent:
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            self.traverse(root.left, to_delete, None, True)
            self.traverse(root.right, to_delete, None, False)
        else:
            if parent is None:
                self.results.append(root)
            self.traverse(root.left, to_delete, root, True)
            self.traverse(root.right, to_delete, root, False)