class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # A kley intuition - you can only sell something you have ALREADY bought
        # You cannot buy from the future and sell in the past.

        max_profit = 0

        buy, sell = 0, 1

        while sell <= len(prices) - 1:

            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

            sell += 1

        return max_profit

            

        