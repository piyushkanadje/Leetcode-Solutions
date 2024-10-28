class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        s= set(nums)
        maxLen=1
        for num in nums:
            if num in s:
                count = 1  
                curr =num**2
                s.remove(num) 

                while curr in s:
                    count+=1
                    s.remove(curr)
                    curr = curr**2
                    
                maxLen = max(count, maxLen)
        
        return -1 if maxLen ==1 else maxLen