class Solution:
    def change(self, amount, coins):
        comp = [0]*(amount+1)
        comp[0] = 1
        curr = [1]
        for c in range(1, len(coins)+1):
            for amt in range(1, amount+1):
                denom = coins[c-1]
                if denom <= amt:
                    curr.append(comp[amt] + curr[amt - denom])
                else:
                    curr.append(comp[amt])
            comp = curr
            curr = [1]
        return comp[-1]