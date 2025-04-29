class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
    #  a + b (target) we will look for target-nums[i] if present take their indices Where to check indices in dictionary
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                return [i, d[target-nums[i]]]
            d[nums[i]] = i

        return []
