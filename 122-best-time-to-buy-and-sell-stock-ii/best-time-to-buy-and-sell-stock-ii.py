class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0


        for index in range(1, n):
            if prices[index] > prices[index-1]:
                max_profit += prices[index]-prices[index-1]
        
        return max_profit
            