class BSTIterator:

    def __init__(self, root):
        self.array = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.array.append(node.val)
            traverse(node.left)

        traverse(root)
        

    def next(self):
        return self.array.pop()
        

    def hasNext(self):
        return len(self.array)