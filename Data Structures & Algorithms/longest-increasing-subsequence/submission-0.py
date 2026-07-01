class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n # longest increasing subsequence till index i
        for i in range(n):
            curr = 0
            for j in range(0 , i):
                if nums[j] < nums[i]:
                    curr = max(curr , dp[j])

            dp[i] += curr
            ans = max(dp[i] , ans)
        return ans