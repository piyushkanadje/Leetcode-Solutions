class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        start = sum(nums)
        summ =0
        for idx , ele in enumerate(nums):
            num = nums[idx]
            if summ == (start - num) / 2:
                return idx
            summ += num
        return -1