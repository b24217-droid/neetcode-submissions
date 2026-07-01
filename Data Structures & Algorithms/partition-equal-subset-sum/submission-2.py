class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True # taking no items and making sum 0 is possible

        for i in range(1 , n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]

    
    def rec(self, i , target , nums):
        if i >= len(nums):
            return False

        if target == 0: # base case
            return True
        if target < 0 :
            return False
        
        # take
        take = self.rec(i + 1 , target - nums[i] , nums)
        # no take
        notake = self.rec(i + 1, target , nums)

        return take or notake

        
