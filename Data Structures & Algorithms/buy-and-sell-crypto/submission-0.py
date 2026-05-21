class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            buy_price = prices[i]

            for j in range(i + 1, len(prices)):
                sell_price = prices[j]
                profit = sell_price - buy_price
                if max_profit < profit:
                    max_profit = profit
        return max_profit