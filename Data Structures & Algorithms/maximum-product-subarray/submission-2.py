class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = [float('-inf')] * (n)
        mini = [float('inf')] * n

        ans = nums[0]

        max_prev = nums[0]
        min_prev = nums[0]

        for i in range(1 , n):
            max_val = max(nums[i] ,max_prev  * nums[i] , min_prev * nums[i])
            min_val = min(nums[i] ,max_prev  * nums[i] , min_prev * nums[i])
            if max_val > ans:
                ans = max_val
            max_prev = max_val
            min_prev = min_val

        return ans