class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        firstString = strs[0]
        lastString = strs[len(strs) -1]
        c = 0
        i=0
        while i < len(firstString) :
            if firstString[i] ==lastString[i]:
                c+=1
            else:
                break
            i+=1
        
        return "" if c == 0 else firstString[0:c]