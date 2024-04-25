class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        index =0 
        ans = []
        for i in range(m):
            new = []
            for j in range(n):
                new.append(original[index])
                index+=1
            ans.append(new)
        return ans
                