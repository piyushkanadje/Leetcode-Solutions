class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        ans =''
        for i in s:
            d[i] = 1 + d.get(i,0)
        
        for i in order:
            if i in order and i in s:
                limit = d.get(i)
                while limit:
                    ans+=i
                    limit-=1
                    d[i]= d.get(i)-1
        for i in d.keys():
            if d[i]>0:
                limit = d.get(i)
                while limit:
                    ans+=i
                    limit-=1
                    d[i]= d.get(i)-1
        
        return ans