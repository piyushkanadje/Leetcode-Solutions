class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s0 = s + s
       # print(s0)
        s1 = s0[1:len(s0)-1]
        #print(s1)
        if s in s1:
            return True
        else :
            return False