class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        i=0
        stack = []
        if len(s)==1:
            return False

        for c in s:
            if c == "{" or c=="[" or c=="(":
                stack.append(c)
            
            else:
                if not stack:
                    return False
                elif stack[-1]=="[" and c !="]":
                    return False
                elif stack[-1] =="{" and c !="}":
                    return False
                elif stack[-1]=="(" and c!=")":
                    return False
                
                stack.pop()
        
        return not stack