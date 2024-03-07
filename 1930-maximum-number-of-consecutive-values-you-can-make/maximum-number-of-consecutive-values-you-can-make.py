class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans=0
        tot=0
        for i in range(len(coins)):
            if tot-coins[i]>=-1:
                tot+=coins[i]
                ans=tot
            else:
                break
        return ans+1


        