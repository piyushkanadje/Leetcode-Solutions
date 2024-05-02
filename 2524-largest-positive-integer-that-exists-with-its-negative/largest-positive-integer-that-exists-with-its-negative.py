class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans  = 0
        for i in range(len(nums)):
            if -nums[i] in nums and nums[i] > ans:
                ans = abs(nums[i])

        return  -1 if ans == 0 else ans
            

        