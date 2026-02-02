class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = collections.defaultdict(int)
        for i in range(len(text)):
            d[text[i]]+=1
        ans = 0
        lCount = d["l"]//2
        oCount = d["o"]//2
        ans = min(d["b"], lCount, oCount, d["n"],d["a"])

        return ans