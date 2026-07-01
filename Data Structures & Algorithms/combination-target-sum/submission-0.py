class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0 , 0 , [] , res , nums,target)
        return res

    def dfs(self , i , curr_sum , curr , res , nums,target):
        if curr_sum  == target:
            res.append(curr.copy())
            return 

        if curr_sum > target or i >= len(nums):
            return 
        
        curr.append(nums[i])
        self.dfs(i, curr_sum + nums[i] , curr , res,nums,target)
        
        curr.pop()
        self.dfs(i + 1 , curr_sum , curr , res,nums,target)

    
