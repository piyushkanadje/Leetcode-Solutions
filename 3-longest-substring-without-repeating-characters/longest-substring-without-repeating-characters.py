class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d= {}
        left = 0 
        ans = 0
        for i in range(len(s)):
            d[s[i]] = 1 + d.get(s[i], 0)

            while d[s[i]] !=1:
                d[s[left]] -=1
                left +=1
                if d[s[left]] ==0:
                    del d[s[left]]
            ans = max(ans, i-left + 1)

        return ans
