class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        count = collections.defaultdict(int)
        count[0]  = 1
        curr = 0
        for num in nums:
            curr +=num %2
            ans += count[curr - k]
            count[curr] += 1
        return ans