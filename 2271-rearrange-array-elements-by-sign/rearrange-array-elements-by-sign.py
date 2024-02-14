class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        n = len(nums)
        ans = [0] * n
        for i in nums:
            if i > 0 and positive < n:
                ans[positive] = i
                positive+=2
            elif i < 0 and negative < n:
                ans[negative] = i
                negative+=2
        return ans
        