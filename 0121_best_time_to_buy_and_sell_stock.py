class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest = float('inf')
        best_profit = 0
        for price in prices:
            if price<cheapest:
                cheapest = price
            else:
                profit =  price - cheapest
                if profit > best_profit:
                    best_profit = profit
        return best_profit
        