class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum  = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[-1])

        for i in range(0, len(nums)-1):
            
            rightSection = prefixSum[-1] - prefixSum[i]
            leftSection = prefixSum[i]
            #print(i,prefixSum[-1],prefixSum[i], rightSection, leftSection)
            if leftSection >= rightSection:
                ans+=1
            

        return ans