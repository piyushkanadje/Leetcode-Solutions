class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])

        curr_end = points[0][1]
        arrow =1

        for point in points[1:]:
            if point[0]  > curr_end:
                arrow+=1
                curr_end = point[1]
            else:
                end = min(curr_end, point[1])
        
        return arrow