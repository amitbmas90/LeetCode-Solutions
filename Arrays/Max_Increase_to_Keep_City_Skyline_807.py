# O(m^2) Runtime and O(m) space complexity, where m is number of rows or columns, which are equal.
# The maximum amount the height can increase is the minimum of max valus of the row and column of the cell.
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        res = 0
        row_max = [-sys.maxsize] * m
        col_max = [-sys.maxsize] * m
        
        for i in range(m):
            for j in range(m):
                if row_max[i] < grid[i][j]:
                    row_max[i] = grid[i][j]
        
        for j in range(m):
            for i in range(m):
                if col_max[j] < grid[i][j]:
                    col_max[j] = grid[i][j]
         
        for i in range(m):
            for j in range(m):
                res += min(row_max[i], col_max[j]) - grid[i][j]
        return res
