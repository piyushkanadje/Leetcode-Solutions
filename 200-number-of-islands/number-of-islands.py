import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row , col = len(grid), len(grid[0])
        visited = set()
        island = 0

        # def bfs(r,c):
        #     queue = collections.deque()
        #     visited.add((r,c))
        #     queue.append((r,c))
        #     while queue:
        #         row, col = queue.popleft()
        #         direction=[[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr, dc in direction:
        #             new_r ,new_c =  row + dr, col + dc
        #             if(new_r in range(row) and new_c in range(col) and grid[new_r][new_c] =="1" and (new_r,new_c) not in visited):
        #                 queue.append((new_r,new_c))
        #            visited.add((new_r,new_c))
        def dfs(r,c):
            if (r not in range(row)or c not in range(col) or grid[r][c]=="0"or (r,c) in visited):
                return
            visited.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(row):
            for c in range(col):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    island+=1
                    dfs(r,c)
                  
        return island
