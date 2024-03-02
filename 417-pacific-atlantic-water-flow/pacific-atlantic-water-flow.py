class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows = len(heights)
        cols = len(heights[0])
        pacificQueue = deque()
        atlanticQueue = deque()
        pacific_visited = [[False] * cols for _ in range(rows)]
        atlantic_visited = [[False] * cols for _ in range(rows)]
        for col in range(cols):
            pacificQueue.append((0,col))
            atlanticQueue.append((rows-1, col))
            pacific_visited[0][col] = True
            atlantic_visited[rows-1][col] = True
        
        for row in range(rows):
            pacificQueue.append((row, 0))
            atlanticQueue.append((row, cols-1))
            pacific_visited[row][0] = True
            atlantic_visited[row][cols-1] = True
        print("Pacific Quqe" , pacificQueue)
        print("Atlantic ", atlanticQueue)
        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                print((row,col))
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r ,c =  row + dr, col + dc
                    if 0<=r < rows and 0 <= c < cols and not visited[r][c]:
                        if heights[r][c] >= heights[row][col]:
                            print("Heights" , heights[r][c])
                            visited[r][c] = True
                            queue.append((r,c))
        
        bfs(pacificQueue, pacific_visited)
        bfs(atlanticQueue, atlantic_visited)

        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i,j])
        
        return result
                

            