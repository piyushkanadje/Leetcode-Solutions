class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr = 0 
        d = defaultdict()
        d[0] =1
        ans = 0
        for i in range(len(nums)):
            curr+=nums[i]%2
            ans +=d.get(curr-k,0)
            d[curr]= 1+ d.get(curr, 0)
        
        return ans