class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currPrefixSum = 0
        ans =0
        count =collections.defaultdict(int)
        count[0]  = 1
        for i in nums:
            currPrefixSum +=i
           
            ans +=count[currPrefixSum - k]
            count[currPrefixSum] =1 + count.get(currPrefixSum, 0)
        return ans