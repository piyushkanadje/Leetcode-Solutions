class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        max_heap = []
        # Push all elements from nums into the max-heap (negated)
        for num in nums:
            heapq.heappush(max_heap, -num)

        while k:
            largest = -heapq.heappop(max_heap)
            score+=largest
            heapq.heappush(max_heap, -(math.ceil(largest/3)))
            k-=1
    
        return score