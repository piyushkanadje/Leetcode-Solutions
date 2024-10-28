class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        