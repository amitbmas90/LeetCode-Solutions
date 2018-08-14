class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0: return 0
        m, n = len(grid), len(grid[0])

        def dfs_by_stack(x, y):
            # search water area from location (x, y) using stack
            # mark cells as visited by marking water from 1 to 0
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        stack.append((nx, ny))

        num_islands = 0

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == '1':
                    num_islands += 1
                    grid[r][c] = '0'
                    dfs_by_stack(r, c)

        return num_islands
