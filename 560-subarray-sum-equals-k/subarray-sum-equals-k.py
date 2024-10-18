class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        ans = 0
        count = collections.defaultdict(int)
        count[0]= 1
        for i in nums:
            curr+=i
            ans +=count[curr-k]
            count[curr] =1  + count.get(curr, 0)
        return ans