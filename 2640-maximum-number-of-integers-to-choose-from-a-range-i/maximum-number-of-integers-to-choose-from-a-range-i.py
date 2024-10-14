class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        summ = 0
        count = 0
        s = set(banned)

        for i in range(1, n+1):
            if i not in s and summ+i <= maxSum:
                summ+=i
                count+=1
        
        return count