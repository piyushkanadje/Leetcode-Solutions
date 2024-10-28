class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(row, col):
            if  0 <= row < len(board) and  0 <= col < len(board[0]):
                return True
            return False
        
        directions= [(1,0),(-1,0),(0,1), (0,-1), (1,1),(-1,1),(-1,-1),(1,-1)]
        rows= len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                countAlive =0
                for x, y in directions:
                    new_row, new_col = i + x, j + y
                    
                    if valid(new_row, new_col) and abs(board[new_row][new_col])==1:
                        countAlive+=1

                if board[i][j] == 1:
                    if countAlive < 2 or countAlive > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if countAlive == 3:
                        board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


