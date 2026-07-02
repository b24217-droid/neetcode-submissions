class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount :
            return 0

        dp = [float('inf')] * (amount + 1) # the number of coins needed to 
        # make sum == i of dp
        dp[0] =  0
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = min(1 + dp[j - coins[i]] , dp[j])

        return dp[amount] if dp[amount] != float('inf') else -1