class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = collections.defaultdict(int)
        
        for i in s:
            d[i]+=1
        check = list(d.values())[0]
        print(d)
        for i in d.values():
            if i != check :
                return False
       
        return True