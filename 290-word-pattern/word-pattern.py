class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")

        if len(s) != len(pattern):
            return False
        ds = {}
        dp ={}

        for i in range(len(pattern)):
            if (pattern[i] not in dp and s[i] not in ds):
                dp[pattern[i]] = s[i]
                ds[s[i]] = pattern[i]
            if ((pattern[i] in dp) and (s[i] not in ds)) or (pattern[i] not in dp and s[i] in ds):
                return False
            if dp[pattern[i]] != s[i]  or ds[s[i]] != pattern[i]:
                return False
        return True
