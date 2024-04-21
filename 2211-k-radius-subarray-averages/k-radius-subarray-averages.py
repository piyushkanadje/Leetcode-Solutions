class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if k > len(nums):
            return [-1]*len(nums)
        ans = [0] * len(nums)
        prefixSum =[nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        print(prefixSum)
        for i in range(len(nums)):
            if i > k-1 and i < len(nums) - k  :
                # print( (prefixSum[i+k] - prefixSum[i-1]))
                print(prefixSum[i-k-1])
                if (i-k-1) < 0:
                    ans[i] = prefixSum[i+k]//(2*k + 1)
                else: 
                    ans[i] = (prefixSum[i+k] - prefixSum[i-k-1])//(2*k + 1)
            else:
                ans[i] = -1
            
        return ans
