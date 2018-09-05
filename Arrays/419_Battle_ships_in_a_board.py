class Solution:
    def countBattleships(self, board):
        """
        One-pass, O(1) space complexity.
        Check if 'X' is left-most point of a ship.
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == 'X':
                    # check left
                    if r > 0 and board[r-1][c] == 'X':
                        continue
                    # check top
                    if c > 0 and board[r][c-1] == 'X':
                        continue
                    res += 1
        return res
