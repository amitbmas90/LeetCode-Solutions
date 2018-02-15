class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == None or len(rooms) == 0: return
        R, C = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        q = collections.deque()
        for r, room in enumerate(rooms):
            for c, cell in enumerate(room):
                if cell == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                x, y = r + dx, c + dy
                if 0 <= x < R and 0 <= y < C and rooms[x][y] == INF:
                    rooms[x][y] = rooms[r][c] + 1
                    q.append((x, y))
