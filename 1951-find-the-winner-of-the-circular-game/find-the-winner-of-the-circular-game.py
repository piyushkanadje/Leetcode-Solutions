class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s = set()
        i=1
        curr =0
        while len(s) < n-1:
            if i not in s:
                curr+=1
                if curr==k:
                    s.add(i)
                    curr = 0
            
            i=i+1
            if i > n:
                i=1
        
        for j in range(1, n+1):
            if j not in s:
                return j

