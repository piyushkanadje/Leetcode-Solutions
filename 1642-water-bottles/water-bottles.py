class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans= numBottles
        empty = numBottles

        while empty>= numExchange:
            fullBottleAfterExchange = empty//numExchange
            empty = (empty % numExchange)+ fullBottleAfterExchange
            ans += fullBottleAfterExchange

        return ans 