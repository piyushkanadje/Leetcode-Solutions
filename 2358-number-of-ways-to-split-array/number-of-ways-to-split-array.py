class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i]+ prefix[i-1])
        for i in range(len(prefix)-1):
            print(prefix[i])
            print(prefix[len(nums)-1] - prefix[i])
            if prefix[i] >= (prefix[len(nums)-1] - prefix[i]):
                print("Hello", i)
                ans+=1
        return ans
        