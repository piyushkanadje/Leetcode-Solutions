class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        print(s)
        for c in s:
            if c== "" or c==".":
                continue
            elif  c=="..":
                if stack:
                    stack.pop()
            elif c!='.' or c !=".." :
                stack.append(c)
    
        ans = "/".join(stack)
        return "/"+ ans