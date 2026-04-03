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
        intervals.sort(key=lambda x: (x.start, x.end))
        currentStart, currentEnd = intervals[0].start, intervals[0].end

        for meeting in intervals[1:]:
            start, end = meeting.start, meeting.end
            if currentEnd <= start: # Finished current interval
                currentStart, currentEnd = start, end
            else: # Meeting interrupted
                return False
        
        return True