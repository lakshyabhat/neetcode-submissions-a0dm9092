"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start= sorted([i.start for i in intervals])
        end= sorted([i.end for i in intervals])
        count,res = 0,0
        sIndex = 0
        eIndex = 0
        while sIndex != len(start):
            if start[sIndex] < end[eIndex]:
                count += 1
                sIndex += 1
            else:
                count -= 1
                eIndex += 1
            res = max(res,count)
        return res
            
            