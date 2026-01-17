class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        ans = 0

        for i in range(k):
            currSum +=nums[i]
        ans = currSum/k
        for j in range(k, len(nums)):
            currSum -= nums[j-k]
            currSum+=nums[j]
            ans = max(ans, currSum/k)

        return ans