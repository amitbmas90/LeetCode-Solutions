# Leetcode 576
# The number of path from each location to the boundary is calculated accumulately.
# For all four directions from location (x, y),
# if the new location is out of bound, add one to the number of paths from that location
# if the new location is within bound, add the number of paths from that location to opt(x,y).
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        res = 0
        
        directions = list(zip([0, 0, 1, -1], [1, -1, 0, 0]))
        
        def inBound(x, y):
            return x >= 0 and x < m and y >= 0 and y < n
        
        for move in range(N):
            temp = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in directions:
                        if inBound(x+dx, y+dy):
                            temp[x][y] += dp[x+dx][y+dy]
                        else:
                            temp[x][y] += 1
                        temp[x][y] %= M
            dp = temp      
        return dp[i][j]
