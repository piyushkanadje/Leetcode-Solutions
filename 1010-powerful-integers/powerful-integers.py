class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i=0
        ans = set()

        if x == 1 and y == 1:
            if bound > 1:
                return [2]
            return []
        elif x == 1:
            j= 0
            ans = []
            while (y ** j) <= bound:
                ans.append((y**j) + 1)
                j+=1
            return ans
        
        elif y ==1:
            j=0
            ans = []
            while (x**j) <= bound:
                ans.append((x**j)+1)
                j+=1
            return ans
   
        while (x ** i) < bound:
            for j in range(0, bound):
                temp = (x ** i) + (y ** j)
                if temp <= bound :
                    ans.add(temp)
                
                else:
                    break
            
            i += 1
         
        return list(ans)
