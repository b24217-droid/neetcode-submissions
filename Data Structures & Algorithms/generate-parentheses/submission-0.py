class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(count_open , count_close , curr):
            if count_open == count_close == 0:
                string = "".join(curr.copy())
                res.append(string)
                return 

            if count_open > 0:
                curr.append("(")
                dfs(count_open - 1 , count_close + 1 , curr)
                curr.pop()

            if count_close > 0:
                curr.append(")")
                dfs(count_open , count_close - 1 , curr)
                curr.pop()

        dfs(n , 0 , [])

        return res