class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        curr = 0
        ans  = 0
        left =0 
        for right in range(len(s)):
            d[s[right]] = 1 + d.get(s[right], 0)
            while d[s[right]] !=1:
                d[s[left]] -=1
                left+=1
                if d[s[left]] == 0:
                    del d[s[left]]
            ans = max(ans, right - left + 1)

        return ans
        