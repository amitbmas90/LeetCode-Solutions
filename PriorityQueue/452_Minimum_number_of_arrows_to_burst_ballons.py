class Solution:
    def findMinArrowShots(self, points):
        """
        Sort points by start value.
        Use max heap to track largest end value.
        if new point start time is less than (or equals to) largest end value,
            update new end value with smaller value
        else add new end value to heap
        return length of heap as result
        :type points: List[List[int]]
        :rtype: int
        """
        import heapq
        heap = []
        points.sort(key=lambda x: x[0])
        for point in points:
            if len(heap) == 0:
                heap.append(-point[1])
            else:
                if point[0] <= -heap[0]:
                    heapq.heapreplace(heap, -min(-heap[0], point[1]))
                else:
                    heapq.heappush(heap, -point[1])
        return len(heap)
