class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counterB = Counter("balloon")
        c = Counter(text)
        ans = float('inf')
        for i in counterB.keys():
            ans = min(c[i]//counterB[i], ans)
        return ans