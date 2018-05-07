class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # -1: live -> death: 2 or 3 live neighbors
        # -2: death -> live: exactly 3 live neighbors
        m, n = len(board), len(board[0])
        
        def liveNeighbors(x, y):
            res = 0
            for dx, dy in zip([0, 0, -1, 1, -1, -1, 1, 1], [1, -1, 0, 0, -1, 1, -1, 1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in {1, -1}:
                    res += 1
            return res
                     
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                num_live_neighbors = liveNeighbors(r, c)
                if board[r][c] == 0 and num_live_neighbors == 3:
                    board[r][c] = -2
                elif board[r][c] == 1 and (num_live_neighbors < 2 or num_live_neighbors > 3):
                    board[r][c] = -1
        
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] == -2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
        
