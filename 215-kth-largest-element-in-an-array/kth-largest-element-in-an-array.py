class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i] * -1)
        
        result = 0
        while k > 0:
            result = heapq.heappop(heap)
            k -= 1
        
        return result * -1