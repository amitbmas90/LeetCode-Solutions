# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# Time-complexity O(IlogI), where I is total number of intervals from all employees.
# Space-complexity O(I).


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        intervals = []
        for s in schedule:
            for interval in s:
                intervals.append(interval)
                
        # sort by start time
        intervals.sort(key = lambda x: x.start)
        
        # merge intervals
        temp = []
        for interval in intervals:
            if not temp or temp[-1].end < interval.start:
                temp.append(interval)
            else:
                temp[-1].end = max(temp[-1].end, interval.end)
                
        res = []
        for i, interval in enumerate(temp):
            if i+1 < len(temp):
                next_ = temp[i+1]
                res.append(Interval(interval.end, next_.start))
        return res
