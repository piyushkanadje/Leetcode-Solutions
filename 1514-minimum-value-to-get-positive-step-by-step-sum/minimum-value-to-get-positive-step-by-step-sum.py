class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal  = 0
        total = 0
        for i in range(len(nums)):
            total = total + nums[i]
            minVal = min(total, minVal)

        return -minVal + 1