class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge_interval  = []
        i = 0
        n= len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merge_interval.append(intervals[i])
            i+=1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0]=min(newInterval[0], intervals[i][0])
            newInterval[1]=max(newInterval[1], intervals[i][1])
            i+=1
        merge_interval.append(newInterval)

        while i < n :
            merge_interval.append(intervals[i])
            i+=1
    
        return merge_interval