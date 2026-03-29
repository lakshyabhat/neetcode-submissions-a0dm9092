class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],x[1]))
        print(intervals)
        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]
        c = 0
        for i in range(1, len(intervals)):
            if currentEnd <= intervals[i][0]:
                currentEnd = intervals[i][1]
            else:
                currentEnd = min(currentEnd,intervals[i][1])
                c += 1

        return c