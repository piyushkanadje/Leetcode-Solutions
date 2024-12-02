class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(' ')

        for i, j in enumerate(s):
            if len(j) >= len(searchWord) and j[:len(searchWord)] == searchWord:
                return i+1
        
        return -1