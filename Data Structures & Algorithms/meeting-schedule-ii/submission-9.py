"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        sidx = 0
        eidx = 0
        res = 0
        count = 0
        while sidx< len(intervals):
            if start[sidx] < end[eidx]:
                count += 1
                sidx += 1
            else:
                count -= 1
                eidx += 1
            res = max(res,count)
        return res

        

'''

        0 ------------------40
            5----10
                    15---20'''

                    