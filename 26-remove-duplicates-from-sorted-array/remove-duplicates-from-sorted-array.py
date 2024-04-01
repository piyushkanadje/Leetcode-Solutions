class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer  = 1
        for i in range(len(nums)):
            if nums[pointer-1] != nums[i]:
                nums[pointer] = nums[i]
                pointer+=1

        return pointer
