class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        def neighbors(x, y, m, n):
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n:
                    yield nx, ny

        if len(rooms) == 0: return

        m, n = len(rooms), len(rooms[0])
        q = collections.deque()

        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                if val == 0:
                    q.append((r, c))

        d = 0

        while q:
            count = len(q)
            for _ in range(count):
                x, y = q.popleft()
                for nx, ny in neighbors(x, y, m, n):
                    if rooms[nx][ny] == 2 ** 31 - 1:
                        rooms[nx][ny] = d + 1
                        q.append((nx, ny))
            d += 1
