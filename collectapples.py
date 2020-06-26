from collections import defaultdict

class Solution:
    def minTime(self, n, edges, hasApple):
        tree = defaultdict(list)
        for edge1, edge2 in edges:
            tree[edge1].append(edge2)
            
        def dfs(node, parent):
            count = 0
            
            for child in tree[node]:
                count += dfs(child, node)
                
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return count + 2
            return count
        return dfs(0, 0)