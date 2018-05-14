# O(M * N) run-time. O(N) space-complexity.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_row, cur_row = None, [0] * n
        cur_row[0] = 1
        for i in range(m):  
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if prev_row:
                        cur_row[j] += prev_row[j]
                    if j > 0:
                        cur_row[j] += cur_row[j-1]
            prev_row = cur_row
            cur_row = [0] * n
        return prev_row[-1]
