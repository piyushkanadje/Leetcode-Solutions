class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit = 0
        minVal = inf
        for i in range(len(prices)):
            minVal = min(minVal, prices[i])
            profit = prices[i] - minVal
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
        