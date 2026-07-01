class Solution:
    def maxArea(self, arr: List[int]) -> int:
        # similar to trapping rain water ??

        l = 0
        r = len(arr) - 1
        ans = 0
        while l < r:
            if arr[l] < arr[r]:
                ans = max(ans , (r - l) * arr[l])
                l += 1
            else:
                ans = max(ans , (r - l) * arr[r])
                r -= 1

        return ans