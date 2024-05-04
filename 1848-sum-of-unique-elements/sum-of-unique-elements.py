class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans =0
        for i in d.keys():
            if d[i] == 1:
                ans+= i
        return ans