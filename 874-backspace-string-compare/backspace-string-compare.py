class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1= []
        stack= []
        for i in s:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
        for j in t:
            if j != "#":
                stack1.append(j)
            elif stack1:
                stack1.pop()
        
        return stack1==stack