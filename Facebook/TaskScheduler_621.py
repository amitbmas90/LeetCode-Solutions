class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        most, K = 0, 0
        d = {}
        for task in tasks:
            if task not in d:
                d[task] = 1
            else:
                d[task] += 1
            if d[task] > most:
                most = d[task]
                K = 1
            elif d[task] == most:
                K += 1
        res = (most-1) * (n+1) + K
        return max(res, len(tasks))
            
