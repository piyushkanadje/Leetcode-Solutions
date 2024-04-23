class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels ="aeiou"
        curr = 0
        ans = 0
        left=0
        for right in range(len(s)):
            if s[right] in vowels:
                curr+=1
            if right - left + 1 > k :
                if s[left] in vowels:
                    curr -=1
                left+=1
            if right - left + 1 == k:
                ans = max(ans, curr)
        return ans
                

            