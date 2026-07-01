class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = [0] * 128
        max_length = 0
        i = 0 
        j = 0

        while j < len(s):
            if curr[ord(s[j])] == 0:
                curr[ord(s[j])] += 1
                max_length = max(max_length , j - i  + 1)       
                j += 1

            else:
                while curr[ord(s[j])] != 0:
                    curr[ord(s[i])] -= 1
                    i += 1


        return max_length
        