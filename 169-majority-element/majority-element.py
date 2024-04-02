class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        
        for i in dict:
            if dict[i] > len(nums)/2:
                return i
        