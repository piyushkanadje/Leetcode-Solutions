class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        

        #here we have 0 indexed nums
        #valid split. at i = == 1 - sum(i+1) >= sum (n-i+1)
        
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
        ans = 0
        for i in range(len(nums)-1):
            if prefix_sum[i] >= prefix_sum[len(nums)-1] - prefix_sum[i+1] + nums[i+1]:
                ans+=1
        
        return ans