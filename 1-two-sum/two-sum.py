class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index , element in enumerate(nums):
            difference = target - element
            if difference in dict : return [dict[difference] , index ]
            dict[element] = index

    