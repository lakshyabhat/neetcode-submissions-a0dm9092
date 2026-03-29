"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i:i.start)
        prevS, prevE = intervals[0].start,  intervals[0].end
        for i in range(1,len(intervals)):
            currS, currE = intervals[i].start,  intervals[i].end
            if prevE > currS:
                return False
            prevE = currE
        return True