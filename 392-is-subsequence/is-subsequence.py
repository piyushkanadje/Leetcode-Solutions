class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0 , 0
        # if len(s) == 1 and len(t)==1:
        #     if s[0] != t[0]:
        #         return False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                print(s[i], t[j])
                i+=1
                j+=1
                print(i)
            else:
                print(t[j])
                j+=1
            
        if i <= len(s)-1: 
            print("I am here", i)
            return False
        
        return True