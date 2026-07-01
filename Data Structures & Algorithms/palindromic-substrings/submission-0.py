class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        if not s :
            return 0

        n = len(s)
        for c_ind in range(n): # c_ind is the index of the center 
            i = c_ind 
            j = c_ind 
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

        for c_ind in range(n): # c_ind is the index of the center 
            i = c_ind 
            j = c_ind + 1
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
        
        return count
            