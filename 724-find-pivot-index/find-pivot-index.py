class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum  = sum(nums)
        start= 0
        for index , value in enumerate(nums):
            if totalSum - value-start== start:
                return index
            start+= value
        
        return -1