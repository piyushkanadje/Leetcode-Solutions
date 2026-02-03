class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        ans = float("inf")
        for  i in range(len(cards)):
            if cards[i]  not in d:
                d[cards[i]] = i
            else:
                ans = min(ans, (i- d[cards[i]]))
                d[cards[i]] = i
        return ans+1 if ans != float("inf") else -1