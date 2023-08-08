class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        maxProfit= 0
        minV = inf
        for i in prices:
            minV= min(i,minV)
            profit = i- minV
            maxProfit=max(profit, maxProfit)
        
        return maxProfit