import collections


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        squares = []
        while i * i <= n:
            squares.append(i * i)
            i += 1
        queue = collections.deque([0])
        visited = set()
        steps = 0
        if n in squares: return 1
        while queue:
            l = len(queue)
            for _ in range(l):
                val = queue.popleft()
                visited.add(val)
                for square in squares:
                    if val + square > n:
                        break
                    elif val + square == n:
                        return steps + 1
                    elif val + square not in visited:
                        queue.append(val + square)
            steps += 1
        return -1
