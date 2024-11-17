class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 
        if target not in nums:
            return -1 
        return nums.index(target)
