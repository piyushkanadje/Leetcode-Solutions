class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(l,r):

            if(l >=rows or r >= cols or l < 0 or r < 0 or grid[l][r]==0):
                return 1
            if (l,r) in visit:
                return 0

            visit.add((l,r))
            perim = dfs(l, r + 1)
            perim += dfs(l + 1, r)
            perim += dfs(l, r - 1)
            perim += dfs(l - 1, r)
            
            return perim
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)