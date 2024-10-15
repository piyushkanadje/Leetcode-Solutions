class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0
        for r in range(n):
            if s[r] == "0":
                res+=(r-l)
                l+=1
        return res