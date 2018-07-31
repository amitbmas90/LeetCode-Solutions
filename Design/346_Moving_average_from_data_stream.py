import collections


class MovingAverage:
    """
    Given a stream of integers and a window size,
    calculate the moving average of all integers in the sliding window.
    """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.cur_sum = 0
        self.queue = collections.deque()
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.cur_sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.cur_sum -= self.queue.popleft()
        return self.cur_sum / len(self.queue)
