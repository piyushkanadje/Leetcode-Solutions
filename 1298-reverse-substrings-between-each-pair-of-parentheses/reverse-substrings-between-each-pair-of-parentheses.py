class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = []
        
        for char in s:
            if char == "(":
                stack.append(len(result))
            elif char == ")":
                start = stack.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(char)
        return "".join(result)