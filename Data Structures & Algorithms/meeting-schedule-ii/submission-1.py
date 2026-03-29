"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : (x.start,x.end))
        if len(intervals)<1:
            return 0
        d = {}
        d[1] = intervals[0]
        for i in range(1,len(intervals)):
            print(intervals[i].start)
            for day,time in d.items():
                if intervals[i].start >= time.end:
                    d[day] = intervals[i]
                    break
            if intervals[i] not in d.values():
                d[max(d.keys()) + 1] = intervals[i]
        return max(d.keys())