class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count = collections.defaultdict(int)
        count[0] = 1
        curr =0
        ans=0
        for right in range(len(nums)):
            curr +=nums[right] %2
            if curr>=k:
                ans+=count[curr-k]
            count[curr]+=1
        return ans