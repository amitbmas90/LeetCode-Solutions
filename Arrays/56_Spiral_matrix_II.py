class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def change_dir(x, y):
            """
            returns True if need to change direction at the location about to visit
            """
            return x < 0 or x == n or y < 0 or y == n or res[x][y] > 0

        if n <= 0:
            return []
        # initialize to -1 to we don't need a map to check visited locations.
        res = [[-1] * n for _ in range(n)]
        # all possible directions
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        cur = 0, -1
        direction = 0

        for val in range(1, n ** 2 + 1):
            x, y = cur
            dx, dy = dirs[direction]
            if change_dir(x + dx, y + dy):
                direction = (direction + 1) % 4
                dx, dy = dirs[direction]
            cur = x + dx, y + dy
            res[cur[0]][cur[1]] = val

        return res
