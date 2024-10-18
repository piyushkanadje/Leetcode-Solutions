class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currPrefixSum = 0
        ans =0
        count =collections.defaultdict(int)
       # We need to initialize counts[0] = 1. This is because the empty prefix [] has a sum of 0. You'll see why this is necessary in a second.
        count[0]  = 1
        for i in nums:
            currPrefixSum +=i
            #prefix sum j to i prefix_sum[j] - prefix_sum[i-1]
            #here prefix_sum[j] - prefix_sum[i-1] = k
            #so prefix_sum[j] - k = prefix_sum[i-1]  means there is subarray with sum k
            ans +=count[currPrefixSum - k]
            count[currPrefixSum] =1 + count.get(currPrefixSum, 0)
        return ans