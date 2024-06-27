class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        count = [0] * (n+2)

        for i in edges:
            count[i[0]]+=1
            count[i[1]]+=1
        for i in range(len(count)):
            if count[i] == len(edges): return i
        
        return -1
