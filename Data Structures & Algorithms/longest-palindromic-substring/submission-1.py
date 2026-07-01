class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        res = ""
        if not s:
            return 0
        n = len(s)
        # for odd length
        for c_ind in range(n):
            i = c_ind
            j = c_ind 
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 >= max_len:
                    res  = s[i:j + 1]
                    max_len = max(max_len , j - i + 1)
                i -= 1
                j += 1

        # for even length
        for c_ind  in range(n):
            i = c_ind 
            j = c_ind + 1
            while i >= 0 and j < n  and s[i] == s[j]:
                if j - i + 1 >= max_len:
                    res = s[i : j + 1]
                    max_len = max(max_len , j - i + 1)
                i -= 1
                j += 1
        return res
        