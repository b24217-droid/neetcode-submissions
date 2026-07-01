class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        prev1 = 0
        prev = 0
        for i in range(2 , n + 1):
            dp[i] = min(prev + cost[i - 1] , prev1  + cost[i - 2])
            prev1 = prev
            prev = dp[i]

        return prev
        