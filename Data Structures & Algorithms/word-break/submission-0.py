class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return 0
        n = len(s)
        dp = [False] * (n + 1) # where we can start
        dp[0] = True

        for end_ind in range(1, n + 1):
            for word in wordDict:
               start_ind =  end_ind - len(word)
               if dp[start_ind] and s[start_ind : end_ind] == word:
                    dp[end_ind] = True

        
        return dp[n]

