class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count  =0 
    
        ans =0 
        for right in range(len(nums)):
            if nums[right] !=0:
                one_count+=1
                ans =max(ans, one_count)
            else:
                one_count=0 
            
        return ans