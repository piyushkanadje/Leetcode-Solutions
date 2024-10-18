class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0:-1}
        curr_sum = 0
        max_len = 0
        for i in range(len(nums)):

            #The core of the problem is finding subarrays with equal numbers of 0s and 1s, which is equivalent to finding subarrays where the sum of the elements is zero if we convert the 0s to -1s.  
            #Then, the problem becomes finding subarrays where the prefix sum is equal to zero, much like the problem you explained about finding subarrays with a sum equal to k.
            if nums[i] == 0:
                curr_sum -=1
            else:
                curr_sum +=1
            
            if curr_sum in prefix_sum:
                max_len= max(max_len, i - prefix_sum[curr_sum])
            else:
                prefix_sum[curr_sum] = i
        
        return max_len