class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =len(matrix)
        col = len(matrix[0])
        # by converting 2d into 1d
        l,h= 0, row*col -1
        count = 0
        while l <= h:
            mid = l + (h-l)//2
           # print("mid, l, h-l",[mid,l,h-l])
            tc = mid % col
            tr = mid // col 
           # print("tr, tc", [tr,tc])
            val = matrix[tr][tc]
            if val == target:
                return True
            if val < target:
                l = mid +1
            else:
                h = mid -1
        return False


