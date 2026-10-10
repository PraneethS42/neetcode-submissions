class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Store dp[i] = fewest coins needed to create i, retrieve dp[n]
        # try to retrieve dp[n]
        dp = [amount+1] * (amount+1) # equivalent to math.inf, most possible to create is amount
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        if dp[amount] == amount+1: #unchanged
            return -1
        else:
            return dp[amount]