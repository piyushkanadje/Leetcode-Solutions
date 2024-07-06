class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time= time % (2*(n-1))
        if n> time:
            return time +1
        else:
            return n - (time- n+1)
        # time = time % (2 * (n - 1))

        # if n > time:
        #     return time + 1
        # else:
        #     return n - (time - n + 1) 