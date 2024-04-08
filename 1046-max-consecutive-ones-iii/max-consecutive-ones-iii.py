class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = 0
        left = 0
        ans= 0
        for right in range(len(nums)):
            #We are counting the number of 0 here 
            if nums[right] == 0:
                curr +=1
            #when the number or zero went from more than k than we are 
            while curr > k:
                if nums[left] == 0:
                    curr -=1
                left +=1
            ans = max(ans , right -left + 1)
                
        return ans
            

