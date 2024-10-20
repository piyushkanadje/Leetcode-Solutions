import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        ans= 0
        while k > 0:
            ele = heapq.heappop(piles)
            heapq.heappush(piles, math.floor(ele/2))
            k-=1
        
        ans = -sum(piles)
    
        return ans
        

