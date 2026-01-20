class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        currSum  = 0
        minVal = 0
        for i in range(len(nums)):
            currSum +=nums[i]
            minVal = min (minVal, currSum)
        return -minVal + 1
