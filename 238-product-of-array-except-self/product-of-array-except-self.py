class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        temp1 = 1
        for i in range(len(nums)):
            ans[i] *= temp1
            temp1*=nums[i]
        
        temp2 = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= temp2
            temp2 *=nums[i]
        
        return ans