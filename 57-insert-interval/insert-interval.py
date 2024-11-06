class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]):
            intervals = sorted(intervals)
            curr= intervals[0]
            ans= []
            ans.append(curr)
            for interval in intervals:
                currBegin = curr[0]
                currEnd= curr[1]
                nextBegin = interval[0]
                nextEnd = interval[1]

                if currEnd >= nextBegin:
                    curr[1] =max(currEnd, nextEnd)
                else:
                    curr= interval
                    ans.append(interval)
            return ans
            
        if len(intervals) ==0:
            return [newInterval]
        lists = intervals
        lists.append(newInterval)
        ans=merge(lists)
        return ans

            