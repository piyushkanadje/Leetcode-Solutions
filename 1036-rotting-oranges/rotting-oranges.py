class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh  = 0
        time = 0
        #Calculate the number or fresh and add rotton to the queue beaacuse while process the loop (while) we need to keep track of the fresh if fresh does not exist what to check then 
        #For each iteration we will increase time
        # If, at the end of the process, some fresh oranges remain (fresh > 0), you return -1 because it means those fresh oranges cannot rot (i.e., they're isolated).


#all the rotten oranges at once by adding them to the queue initially. This allows the BFS to spread the rot to neighboring oranges level by level (minute by minute). This is also known as a multi-source BFS,
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c] ==2  :
                    queue.append((r,c))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while queue and fresh > 0 :
            length= len(queue)
            for i in range(length):
                r , c  = queue.popleft()
                for dr , dc in directions:
                    row = r + dr 
                    col = c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2 
                        queue.append((row,col))
                        fresh -= 1
            time+=1

        return time if fresh == 0 else -1

