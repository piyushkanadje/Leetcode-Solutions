class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        l , r = 0 , n-1
        ans = 0
        while l < r:
            while s[l] == "0" and l < n-1 : l+=1
            while s[r] =="1" and r>0 : r-=1

            if l < r and s[l] == "1" and s[r] == "0":
                ans+=(r-l)
                l+=1
                r-=1
            
        return ans