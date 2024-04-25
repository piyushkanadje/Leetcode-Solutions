class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        if m*n==len(original):
            for i in range(m):
                
                res.append(original[i*n:i*n+n])
               
        return res