class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return

        def dfs(x, y):
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = 'V'
                    dfs(nx, ny)

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        border = ([(0, i) for i in range(n)] +
                  [(m - 1, i) for i in range(n)] +
                  [(i, 0) for i in range(m)] +
                  [(i, n - 1) for i in range(m)])

        for x, y in border:
            if board[x][y] == 'O' and not visited[x][y]:
                visited[x][y] = True
                board[x][y] = 'V'
                dfs(x, y)

        for row in board:
            for col, val in enumerate(row):
                row[col] = 'XO'[val == 'V']
