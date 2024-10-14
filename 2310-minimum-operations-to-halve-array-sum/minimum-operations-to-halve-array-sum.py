class Solution:
    def halveArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        arr_sum = sum(nums)/2
        summ=0
        arr = [-num for num in nums]
        heapq.heapify(arr)
        count = 0
        while arr_sum > summ:
            largest = - heapq.heappop(arr)
            summ+=largest/2
            heapq.heappush(arr, -(largest/2))
            count+=1
        
        return count
