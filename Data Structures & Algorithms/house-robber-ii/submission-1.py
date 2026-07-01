class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:return 0
        if n == 1:
            return nums[0]
        op1 = self.solve( nums[0:n-1])
        op2 = self.solve( nums[1:])
        return max(op1 , op2)

    def solve(self , nums):
        ans = 0
        n = len(nums)
        if not nums:
            return 0
        if len(nums ) <= 2:
            return max(nums)

        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[1] , nums[0])

        for i in range(2 , n):
            dp[i] = max(dp[i - 1] , dp[i - 2] + nums[i])

        return dp[-1]