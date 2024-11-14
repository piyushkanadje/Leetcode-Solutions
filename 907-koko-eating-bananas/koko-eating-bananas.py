class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkSpeed(k):
            hours= 0

            for pile in piles:
                hours+=ceil(pile/k)

            return hours <= h

        low= 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            if checkSpeed(mid):
                high = mid -1
            else:
                low = mid + 1
        
        return low