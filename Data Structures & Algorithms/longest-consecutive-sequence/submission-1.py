class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0 
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen : # start of the sequence
                j = 1 
                while num + j in seen:
                    j += 1 
                maxlen = max(maxlen , j)

        return maxlen
        