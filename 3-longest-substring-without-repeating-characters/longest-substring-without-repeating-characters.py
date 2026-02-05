class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}   
        left = 0
        ans = 0
        for right in range(len(s)):
            d[s[right]] = d.get(s[right],0) +1
            while d[s[right]]> 1:
                d[s[left]] -=1
                if d[s[left]] == 0:
                    del d[s[left]]
                left +=1
            ans = max(ans, right- left + 1)

        return ans