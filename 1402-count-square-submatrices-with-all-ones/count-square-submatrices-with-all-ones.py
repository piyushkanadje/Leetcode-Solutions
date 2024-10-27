class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS= len(matrix)
        COLS= len(matrix[0])

        cached = {}

        #For searching all the positions
        def dfs(r, c):
            # check boundry condition and check it matrix[row][col] is 0 if zero return 0
            if r == ROWS or c == COLS or not matrix[r][c]:
                return 0
            if (r,c) in cached:
                return cached[(r,c)]
            #why 1 because we are already checking the matrix[row][col] == 1 if its 1 then there is a square
            #Lenght =1
            #Now we are cheching down, right and diagonally and checking that do we have all the 1's on that position if yes then we will add 1
            cached[(r,c)] = 1 +  min(
                dfs(r+1, c),
                dfs(r, c+1),
                dfs(r+1, c+1)
            )

            return cached[(r,c)]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r,c)
        
        return res
