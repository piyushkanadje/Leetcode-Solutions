class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroCount = 0
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if zeroCount > 0 and s[i] == "1":
                ans+=zeroCount
            if s[i]=="0":
                zeroCount+=1
        
        return ans