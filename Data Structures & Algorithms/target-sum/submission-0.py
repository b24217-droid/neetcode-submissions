class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(i , target , curr_sum ):

            if target == curr_sum and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            
            
            # take positive nums
            take = rec(i + 1 , target  ,curr_sum + nums[i])
            notake = rec(i + 1 , target , curr_sum - nums[i])

            return take + notake

        return rec(0 , target , 0)

        