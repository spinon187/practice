class Solution:
    def coinChange(self, coins, amount):
        ways = [amount+1 for _ in range(amount + 1)]
        ways[0] = 0
        for coin in coins:
            for i in range(coin, len(ways)):
                ways[i] = min(ways[i], ways[i - coin] + 1)
                
        return ways[amount] if ways[amount] != amount+1 else -1