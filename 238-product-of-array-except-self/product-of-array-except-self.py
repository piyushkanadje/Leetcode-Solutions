class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        temp1= 1
        for i in range(n):
            ans[i] = temp1
            temp1 *=nums[i]
        
        temp2 =1 
        for i in range(n-1,-1,-1):
            ans[i] *= temp2
            temp2 *= nums[i]
        
        return ans
            