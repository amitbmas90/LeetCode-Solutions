class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def neighbors(x, y):
            for nx, ny in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                if 0 <= nx < m and 0 <= ny < n:
                    yield nx, ny

        def dfs(x, y, cache):
            """
            dfs with memorization
            effectively divide the problem to m * n subproblems
            """
            if (x, y) not in cache:
                res = 0
                for nx, ny in neighbors(x, y):
                    if matrix[x][y] < matrix[nx][ny]:
                        res = max(res, dfs(nx, ny, cache))
                res += 1
                cache[x, y] = res
            return cache[x, y]

        if len(matrix) == 0: return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        cache = {}

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                res = max(res, dfs(r, c, cache))
        return res
