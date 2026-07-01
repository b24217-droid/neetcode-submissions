class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices :
            return 0

        buying_price = prices[0]
        selling_price = prices[0]
        for price in prices:
            if price < buying_price:
                buying_price = price
            else:
                selling_price = price
                profit = max(profit , selling_price - buying_price)

        return profit
