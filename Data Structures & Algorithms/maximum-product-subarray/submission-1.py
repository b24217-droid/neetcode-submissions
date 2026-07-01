class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = [float('-inf')] * (n)
        mini = [float('inf')] * n

        ans = nums[0]

        maxi[0] = nums[0]
        mini[0] = nums[0]

        for i in range(1 , n):
            maxi[i] = max(nums[i] ,maxi[i - 1]  * nums[i] , mini[i - 1] * nums[i])
            mini[i] = min(nums[i] ,maxi[i - 1]  * nums[i] , mini[i - 1] * nums[i])
            if maxi[i] > ans:
                ans = maxi[i]

        return ans