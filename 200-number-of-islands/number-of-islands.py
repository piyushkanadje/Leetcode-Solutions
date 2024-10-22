class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            for row, col in directions:
                new_row , new_col = i+ row, j+col
                if 0<= new_row < len(grid) and 0<= new_col < len(grid[0]) and grid[new_row][new_col] =="1" and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col)
                    

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        island = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    island+=1
                    visited.add((i,j))
                    dfs(i,j)

        return island

