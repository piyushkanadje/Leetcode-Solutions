class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        maxi = max(d.values())
        count = 0
        for i in d.keys():
            if d[i] == maxi:
                count+=maxi
        
        return count
