class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = set()
        for i in range(len(s)):
            if s[i] in d:
                return s[i]
            d.add(s[i])