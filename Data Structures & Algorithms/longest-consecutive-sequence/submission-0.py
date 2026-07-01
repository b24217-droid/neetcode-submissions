class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        curr_lens = 0
        for num in seen:
            if (num - 1) not in seen: # that means it is the start of a seq
                curr_len = 1
                while num + curr_len in seen:
                    curr_len += 1
                longest = max(longest , curr_len)
        
        return longest


