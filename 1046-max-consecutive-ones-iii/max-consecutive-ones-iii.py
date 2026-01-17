class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left  =0 
        currZero = 0
        ans =0
        for right in range(len(nums)):
            if nums[right] == 0:
                currZero += 1

            while currZero > k:
                if nums[left]== 0:
                    currZero -=1
                left +=1
            ans = max(ans, right- left +1)
        return ans