class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_make = 1
        for coin in coins:
            if coin<= max_make:
                max_make +=coin
        return max_make