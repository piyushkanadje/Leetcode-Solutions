class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for [x, cnt] in Counter(nums).items():
            if cnt * 2 >= len(nums):
                return x

        return -1
        