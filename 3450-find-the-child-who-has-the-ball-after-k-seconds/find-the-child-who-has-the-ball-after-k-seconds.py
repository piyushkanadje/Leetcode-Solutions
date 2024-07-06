class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        fullRound= k// (n-1)
        extraTime = k %(n-1)

        if fullRound %2 == 0:
            return extraTime
        else:
            return (n-1) - extraTime