from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max_heap stores smaller half
        # min_heap stores larger half
        self.heaps = ([], [])


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        max_heap, min_heap = self.heaps
        if len(max_heap) == len(min_heap):
            if len(min_heap) > 0 and min_heap[0] < num:
                heappush(max_heap, -heappop(min_heap))
                heappush(min_heap, num)
            else:
                # give the number to max_heap
                heappush(max_heap, -num)
        else:
            # median is -max_heap[0]
            if -max_heap[0] >= num:
                heappush(min_heap, -heappop(max_heap))
                heappush(max_heap, -num)
            else:
                heappush(min_heap, num)


    def findMedian(self):
        """
        :rtype: float
        """
        max_heap, min_heap = self.heaps
        if len(max_heap) > len(min_heap):
            return -max_heap[0] / 1.0
        return (min_heap[0] - max_heap[0]) / 2.0
