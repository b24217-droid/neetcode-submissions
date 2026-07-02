class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(i , curr):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            
            curr.append(nums[i])
            take = rec(i + 1 , curr)
            curr.pop()
            notake = rec(i + 1 , curr)

        rec(0 , [])
        return res
