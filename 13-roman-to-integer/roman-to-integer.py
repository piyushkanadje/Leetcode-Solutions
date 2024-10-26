class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        count=0
        count+=roman[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] >= roman[s[i+1]]:
                count+=roman[s[i]]
            else:
                count-=roman[s[i]]
        return count
