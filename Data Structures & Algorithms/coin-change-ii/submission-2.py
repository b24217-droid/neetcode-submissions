class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0] * (amount + 1)
        prev[0] = 1

        for i in range(1 , n + 1):
            for j in range(1 , amount + 1):
                if coins[i - 1] <= j:
                    prev[j] += prev[j - coins[i - 1]]
        return prev[amount]