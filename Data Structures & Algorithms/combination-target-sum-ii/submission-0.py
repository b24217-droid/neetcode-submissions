class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i , candidates , target, curr, res):
            # if we are not taking a number that means we cannot take any of 
            # its duplicate too

            if target == 0:
                res.append(curr.copy())
                return 

            if target < 0 or i >= len(candidates):
                return 

            # taking
            curr.append(candidates[i])
            dfs(i + 1 , candidates , target -candidates[i] , curr , res)

            curr.pop()
            # if we are not taking that means we will not take any of dups
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j , candidates , target , curr , res)

        dfs(0 , candidates , target , [] , res)
        return res