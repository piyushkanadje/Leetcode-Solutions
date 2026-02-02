class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        curr = 0

        for i , num in enumerate(nums):
            curr +=1 if nums[i] == 1 else -1
            if curr == 0:
                ans = i +1
            elif (curr in d):
                ans = max(ans, i- d[curr])
            else:
                d[curr] = i
        
        return ans