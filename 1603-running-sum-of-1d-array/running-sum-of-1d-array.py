class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            current = nums[i]
            nums[i] = current + nums[i-1]

        return nums
        