class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i , nums , curr):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            
            curr.append(nums[i])
            dfs(i + 1 , nums , curr)

            curr.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j , nums , curr)

        dfs(0 , nums , [])
        return res
