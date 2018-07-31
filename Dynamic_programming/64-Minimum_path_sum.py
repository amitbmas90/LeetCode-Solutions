import sys


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j != n-1:
                    dp[j] = grid[i][j] + dp[j+1]
                elif i != m-1 and j == n-1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != m-1 and j != n-1:
                    dp[j] = grid[i][j] + min(dp[j+1], dp[j])
                else:
                    dp[j] = grid[i][j]
        return dp[0]


class Solution_top_down:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        opt = {(m - 1, n - 1): grid[m - 1][n - 1]}

        def dp(x, y):
            # solves the subproblem of finding minimal path sum to bottom-right location from location x, y
            if (x, y) not in opt:
                if x < 0 or x == m or y < 0 or y == n:
                    return sys.maxsize
                res = grid[x][y] + min(dp(x + 1, y), dp(x, y + 1))
                opt[x, y] = res
            return opt[x, y]

        dp(0, 0)
        return opt[0, 0]
