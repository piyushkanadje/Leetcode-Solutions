class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans= numBottles
        empty = numBottles

        while empty>= numExchange:
            fullBottleAfterExchange = empty//numExchange
            print(fullBottleAfterExchange)
            empty = (empty % numExchange)+ fullBottleAfterExchange
            ans += fullBottleAfterExchange

        return ans 