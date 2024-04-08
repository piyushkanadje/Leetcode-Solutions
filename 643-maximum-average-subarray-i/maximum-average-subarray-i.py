class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        
        for i in range(k):
            summ += nums[i]
        
        average = summ/k
        ans = average
        for i in range(k, len(nums)):
            summ +=nums[i]
            summ -= nums[i-k]
            ans = max(summ/k, ans )
        
        return ans