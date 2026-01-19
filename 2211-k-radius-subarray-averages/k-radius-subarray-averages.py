class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        
        if k == 0:
            return nums
        
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        for i in range(k, n - k):
            left = i - k
            right = i + k
            
            if left == 0:
                window_sum = prefixSum[right]
            else:
                window_sum = prefixSum[right] - prefixSum[left - 1]
            
            ans[i] = window_sum // (2 * k + 1)
        
        return ans
