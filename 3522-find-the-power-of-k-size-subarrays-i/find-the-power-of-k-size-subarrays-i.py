class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        arr = [False] * len(nums)
        arr[0] = True

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                arr[i] = True
        
        falseCount = 0

        for i in range(k):
            if arr[i] == False:
                falseCount += 1
        
        l = 0
        r = k-1
        ans = []
        while r < len(nums):

            
            

            if falseCount == 0:
                ans.append(nums[r])
            
            elif falseCount == 1 and arr[l] == False:
                ans.append(nums[r])
            
            else:
                ans.append(-1)
            
            
            
            l += 1
            r += 1

            if arr[l-1] == False:
                falseCount -= 1
            if r != len(nums):
                if arr[r] == False:
                    falseCount += 1



            
        
        return ans
