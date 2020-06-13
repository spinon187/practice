class Solution:
    def combinationSum(self, candidates, target):
        dp = {}
        dp[0] = [[]]
        candidates.sort()
        for c in candidates:
            for t in range(c, target + 1):
                if (t-c) in dp:
                    if t not in dp:
                        dp[t] = []
                    for comb in dp[t-c]:
                        dp[t].append(comb + [c])
        return dp[target] if target in dp else []