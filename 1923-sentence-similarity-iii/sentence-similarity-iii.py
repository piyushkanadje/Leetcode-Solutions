class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a  = sentence1.strip().split(' ')
        b = sentence2.strip().split()

        n = len(a)
        m  = len(b)
        print(n,m, a, b)
        if n < m:
            a , b = b,a
            m=n
        i = 0
        while i < m and a[i] == b[i] :
            i+=1
        #Means both strings are same 
        if i==m:
            return True

        j = 0
        while j < m - i and a[-1 -j ] == b [-1 - j]:
            j+=1
        
        return i+j == m
