class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if n <= k :
            return "0"
        stack = []
        for i , ele in enumerate(num):
            while k > 0 and stack and ele < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(ele)
        while k > 0:
            stack.pop()
            k-=1
        ans = ''.join(stack).lstrip('0')
        return ans if ans else "0"