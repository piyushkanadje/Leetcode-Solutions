class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # there are 3 different way we can solve this problem 
        #1-brute fouce with 2 for loop
        #2- applying binary search to 2d matrix
        #3- by converting 2d matrix into 1d

        #2

        row  = 0
        col = len(matrix[row]) - 1

        while  row  < len(matrix) and col >=0:
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                row +=1
            else:
                col -=1
        return False

        # #3

        # row = len(matrix)
        # col = len(matrix[0])
        # l , h = 0 , row*col -1

        # while l < h:



        
 
        
    
