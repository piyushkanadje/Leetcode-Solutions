class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
                continue
            
            if i==")" and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)

        return len(stack) 