class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        left = 0
        ans= 0
        if k <= len(s):

            for i in range(k):
                if s[i] in vowels:
                    count+=1
            ans  = count
            for right in range(k, len(s)):
                if s[right-k] in vowels:
                    count-=1
    
                if s[right]in vowels:
                    count+=1
                ans = max(ans, count)
        return ans
            
