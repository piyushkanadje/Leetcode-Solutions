class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum  = 0
        left  =0
        ans = float('inf')
        for right in range(len(nums)):
            currSum+=nums[right]
            while currSum >= target:
                ans = min(ans, right - left + 1)
                currSum-=nums[left]
                left+=1
        
        return ans if ans != float('inf') else 0