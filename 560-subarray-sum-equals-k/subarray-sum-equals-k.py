class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        # I tried this problem by using brute force then problem comes to n2 then with prefix s
        #sum only the problem is again n2 same thing to calculate the subaary with the sam sum

        #With hashmap, the idea is:
        # If there exists an index i such that
        # prefixSum[j] = prefixSum[i] + k
        # (i.e., prefixSum[j] - prefixSum[i] = k),
        # then the subarray from (i + 1) to j has sum k.

        #if the prefixSum[j] - prefixSum[i]  = 0 means they are equal that means the sum between 2 is 0
        #so here we store the prefixSum of each time and check and to get our ans currSum - k and check if this presents or not if this presents means we can remove this for this much times to get he required sum

        #here we are adding zero because lets say if we get curr-k = 0 and we do not have a subarray which is same then we would lost the valid subarray


        currSum = 0
        hashMap = {0:1}
        ans = 0
        for i in range(len(nums)): 
            currSum += nums[i]
            if currSum - k in hashMap:
                ans +=hashMap[currSum-k]
            hashMap[currSum] = 1 + hashMap.get(currSum,0)

        return ans
            

