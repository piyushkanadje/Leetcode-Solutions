class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]: 
        d = collections.defaultdict(int)
        for i , j in matches:
            d[i]+=0
            d[j]+=1
        
        zeroLost = []
        oneLost = []
        for i in d.keys():
            if d[i]==0:
                zeroLost.append(i)
            if d[i] ==1:
                oneLost.append(i)

        return [sorted(zeroLost),sorted(oneLost)]
        




