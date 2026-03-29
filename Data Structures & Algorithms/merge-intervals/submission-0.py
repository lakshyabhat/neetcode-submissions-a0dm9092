class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]
        merge = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= currentEnd:
                currentEnd = max(currentEnd,intervals[i][1])
            else:
                merge.append([currentStart,currentEnd])
                currentStart = intervals[i][0]
                currentEnd = intervals[i][1]
        merge.append([currentStart,currentEnd])
        
        return merge
