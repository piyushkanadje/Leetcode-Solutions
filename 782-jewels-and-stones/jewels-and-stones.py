class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = Counter(stones)
        count = 0
        for i in jewels:
            if i in d:
                count+=d[i]
        return count
