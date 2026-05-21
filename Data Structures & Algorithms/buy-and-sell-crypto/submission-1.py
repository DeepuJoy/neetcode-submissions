class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_seen_price = 101
        for i in range(len(prices)):
            if lowest_seen_price > prices[i]:
                lowest_seen_price = prices[i]
            else:
                profit = prices[i] - lowest_seen_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
