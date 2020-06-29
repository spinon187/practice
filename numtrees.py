from collections import defaultdict

class Solution:
    def numTrees(self, n):
        d = defaultdict(int)
        d[0], d[1] = 1, 1
        if n <= 1:
            return(d[n])
        
        for i in range(2, n+1):
            for j in range(i):
                d[i] += d[j]*d[i-j-1]
        
        return d[n]