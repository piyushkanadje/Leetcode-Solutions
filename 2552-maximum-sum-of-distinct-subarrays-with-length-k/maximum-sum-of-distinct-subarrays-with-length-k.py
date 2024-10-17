class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, r = 0 , 0
        
        ms , total = 0 , 0 
        s = set()
        while r < len(nums):
            while nums[r] in s:
             
                total -=nums[l]
                s.remove(nums[l])
                l+=1
                
            total +=nums[r]
            s.add(nums[r])
            
            if (r - l +1)==k:
                ms= max(ms, total)
                total -=nums[l]
                s.remove(nums[l])
                l+=1
            
            r+=1
        
        return ms
