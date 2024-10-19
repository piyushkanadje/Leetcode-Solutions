class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence( word: str) -> bool:
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        count=0
        for word in words:
            if isSubsequence(word):
                count+=1
        return count