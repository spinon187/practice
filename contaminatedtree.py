class FindElements:

    def __init__(self, root):
        self.root = root
        self.root.val = 0
        self.cheese = set()
        self.traverse(self.root)
        
    def traverse(self, node):
        self.cheese.add(node.val)
        if node.left:
            node.left.val = 2*node.val + 1
            self.traverse(node.left)
        if node.right:
            node.right.val = 2*node.val + 2
            self.traverse(node.right)

    def find(self, target):
        return target in self.cheese