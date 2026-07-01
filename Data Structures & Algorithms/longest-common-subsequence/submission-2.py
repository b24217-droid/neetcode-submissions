class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        prev = [0 for _ in range(len(text1) + 1)]

        for i in range(1 , len(text2) + 1):
            curr = prev.copy()
            for j in range(1 , len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    curr[j] = 1 + prev[j - 1]

            
                else:
                    curr[j] = max(prev[j] , curr[j - 1])
            prev = curr.copy()
        return prev[len(text1)]