class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        left = 0
        ans = 0
        letter = {}
        for right in range(len(s)):
            letter[s[right]] = 1 + letter.get(s[right],0)
            maxF = max(maxF,  letter[s[right]] )

            if (right -  left + 1 ) - maxF > k:
                letter[s[left]] -=1
                left+=1
            
            ans = max(ans , right - left +1)

        
        return ans


