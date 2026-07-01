class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mini = float('inf')

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < mini:
                mini = nums[mid]

            if nums[low] < nums[high]:
                high = mid - 1
            elif nums[low] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return mini

