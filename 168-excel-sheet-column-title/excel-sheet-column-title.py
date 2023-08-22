class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            out = chr(ord('A') + (columnNumber -1)%26) + out
            columnNumber = (columnNumber - 1) //26
        
        return out