class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        if n ==1:
            return s
        
        count = {}
        vowles ="aeiouAEIOU"

        for i in s:
            if i in vowles:
                count[i]= 1 + count.get(i,0)
        res =[]
        def findVowels():
            mini = 'z'
            for k ,v in count.items():
                if mini > k:
                    mini= k
            if count[mini] == 1:
                count.pop(mini) 
            else:
                count[mini] -= 1
            return mini

        for char in s:
            if char in vowles:
                res.append(findVowels())
            else:
                res.append(char)

        return "".join(res)