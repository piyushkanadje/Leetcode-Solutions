class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans=0
        happiness.sort()
        for i in range(k):
            a=happiness.pop()
            if a-i>=0:
                ans+=a-i
        return ans