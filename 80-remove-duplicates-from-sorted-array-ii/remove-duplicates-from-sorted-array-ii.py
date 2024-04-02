class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentElement = nums[0]
        currentCount = 1
        left = 1

        for i in range(1, len(nums)):
            loopElement = nums[i]
            if currentElement != loopElement:
                nums[left] = loopElement
                left +=1
                currentElement = loopElement
                currentCount = 1
                continue
            
            if currentCount >=2:
                continue
            
            nums[left] = loopElement
            left+=1
            currentCount+=1
        
        return left

