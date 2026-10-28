class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for ind , num in enumerate(nums):
            diff = target - num 
            if diff in mp :
                return sorted([mp[diff] , ind])

            mp[num] = ind
         
        return (-1 , -1)

        