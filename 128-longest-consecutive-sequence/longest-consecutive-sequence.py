class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set
        ans = set()
        for i in nums:
            ans.add(i)
        
        currElement = 0
        currentCount = 0 
        count = 0
        for i in nums:
            currElement = i
            currentCount = 1
            if currElement-1 not in ans:

                while currElement + 1 in ans:
                    currentCount +=1
                    currElement+=1
            
            count = max(count, currentCount)
        return count