class Solution:
    def __init__(self):
        self.counts = {}
        self.max_freq = 0
        self.most_frequent = []
    
    def findFrequentTreeSum(self, root):
        
        def traverse(node):
            if not node:
                return 0
            subtreeSum = node.val + traverse(node.left) + traverse(node.right)
            if subtreeSum not in self.counts:
                self.counts[subtreeSum] = 0
            self.counts[subtreeSum] += 1
            if self.counts[subtreeSum] == self.max_freq:
                self.most_frequent.append(subtreeSum)
            elif self.counts[subtreeSum] > self.max_freq:
                self.most_frequent = [subtreeSum]
                self.max_freq = self.counts[subtreeSum]
            return subtreeSum
        
        traverse(root)
        return self.most_frequent