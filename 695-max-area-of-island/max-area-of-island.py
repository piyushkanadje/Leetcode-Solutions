class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount = 0
        row , col = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (
                r < 0
                or r == row
                or c < 0
                or c == col
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            visited.add((r,c))
            area = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                area +=dfs(r+dr, c+dc)
            return area
        for r in range(row):
            for c in range(col):
                maxCount = max(maxCount, dfs(r,c))
        return maxCount