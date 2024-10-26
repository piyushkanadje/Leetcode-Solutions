class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        li = list(s.split(" "))
        l = 0
        r= len(li) - 1
        print(li)   
     
        while l < r:
            li[l] , li[r] = li[r], li[l]
            l+=1
            r-=1
        ans = ""
        for i in li:
            if i != "":
                ans= ans + " "+ i

        return ans.strip()

        