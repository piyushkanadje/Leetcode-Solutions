class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [""]*len(s.split())
        for i in s.split(' '):
            index = int(i[-1]) - 1
            arr[index] = i[0:len(i)-1]
        sen = ""
        for i in arr:
            sen+=(i+' ')
        
        return sen.strip()
            