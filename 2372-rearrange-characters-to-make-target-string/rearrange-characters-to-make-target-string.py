class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counterB = Counter(target)
        c = Counter(s)
        ans = float('inf')
        for i in counterB.keys():
            ans = min(c[i]//counterB[i], ans)
        return ans