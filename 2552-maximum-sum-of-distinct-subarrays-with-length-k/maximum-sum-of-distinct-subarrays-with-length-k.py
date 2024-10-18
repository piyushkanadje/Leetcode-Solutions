class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0 
        total = 0
        r= 0
        s = set()
        while r < len(nums):

            while nums[r] in s:
                total-=nums[left]
                s.remove(nums[left])
                left+=1
                
            total +=nums[r]
            s.add(nums[r])

            if(r - left + 1)==k:
                ans = max(total, ans)
                total -=nums[left]
                s.remove(nums[left])
                left+=1
            
            r+=1
        
        return ans