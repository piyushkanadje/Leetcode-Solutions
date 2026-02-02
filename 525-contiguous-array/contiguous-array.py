class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val= 0
        max_lel= 0
        for i , num in enumerate(nums):
            sum_val +=1 if num==1 else -1
            if sum_val == 0:
                max_lel=i+1
            elif(sum_val in mp):
                max_lel = max(max_lel, i - mp[sum_val])
            else:
                mp[sum_val] = i
            
        return max_lel