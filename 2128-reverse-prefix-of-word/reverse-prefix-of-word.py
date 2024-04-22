class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        i=0
        for j in range(len(word)):
            if word[j]==ch:
                break
        if j!=len(word)-1 or word[j]== ch:
            while i < j:
                word[i], word[j] = word[j], word[i]
                i+=1
                j-=1
        return "".join(word)