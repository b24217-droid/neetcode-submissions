class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(0 , nums , [] , res)
        return res

    def helper(self , i, nums , curr,res):
        if i >= len(nums):
            res.append(curr)
            return 

        take = self.helper(i  + 1, nums , curr + [nums[i]] ,res)
        notake = self.helper(i + 1 , nums , curr, res)

        
        