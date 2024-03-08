class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        n = max(f.values())
        s=0
        for x in nums:
            if(f[x] == n):
                s+=1
        return s