class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            if nums[i]>0 and nums[i]>ans:
                if (nums[i]*-1) in nums:
                    ans=nums[i]
        return ans
            

        