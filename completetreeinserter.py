class CBTInserter:

    def __init__(self, root):
        self.root = root
        self.arr = []
        q = [root]
        while q:
            curr = q.pop(0)
            self.arr.append(curr)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    def insert(self, v):
        new_node = TreeNode(v)
        self.arr.append(new_node)
        parent = self.arr[(len(self.arr)-2)//2]
        if len(self.arr) % 2:
            parent.right = new_node
        else:
            parent.left = new_node
        return parent.val
        
    def get_root(self):
        return self.root
