class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in arr:
            if i * 2 in d or i/2 in d:
                return True
            d[i]+=1
        
        return False