class Solution:

    
    def nextGreator(self,nums: List[int])-> List[int]:
        stack = []
        result  = [-1]*len(nums)

        for i in range(len(nums)):
            while stack  and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)
        
        return result
                
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = self.nextGreator(nums2)
        ans = []
        for i in nums1:
            ans.append(result[nums2.index(i)])
            
        return ans
