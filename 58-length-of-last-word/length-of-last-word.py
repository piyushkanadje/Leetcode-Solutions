class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        slist= s.split(' ')
        return len(slist[-1])