class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        
        maxVal = max(dict.values())

        for i in dict:
            if dict[i] == maxVal:
                return  i
        