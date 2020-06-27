class Solution:
    def distanceK(self, root, target, K):
        graph = {}
        
        def dfs(node, graph, parent):
            if not node:
                return
            
            if node.val not in graph:
                graph[node.val] = []
            if parent is not None:
                graph[node.val].append(parent)
                graph[parent].append(node.val)
            
            dfs(node.left, graph, node.val)
            dfs(node.right, graph, node.val)
        
        dfs(root, graph, None)
            
        seen = set([target.val])
        q = [target.val]
        while K > 0:
            K -= 1
            next_round = []
            for node in q:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        next_round.append(neighbor)
            q = next_round
        
        return q 