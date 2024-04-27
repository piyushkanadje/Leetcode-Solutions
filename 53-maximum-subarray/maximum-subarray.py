class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        res= nums[0]

        for i in range(1, len(nums)):
            maxSum = max(maxSum + nums[i], nums[i])
            res = max(maxSum , res)

        return res  