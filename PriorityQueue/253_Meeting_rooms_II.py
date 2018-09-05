# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heapreplace, heappush
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        """
            sort intervals by starting time
        """
        intervals.sort(key = lambda x: x.start)
        heap = []
        """
            min-heap maintains ending time for all meeting rooms
            heap top value is the earliest time
        """
        for interval in intervals:
            start_time, end_time = interval.start, interval.end
            if len(heap) == 0 or heap[0] > start_time:
                heappush(heap, end_time)
            else:
                heapreplace(heap, end_time)
        return len(heap)
