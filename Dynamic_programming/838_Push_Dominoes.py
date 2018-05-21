class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        f = 0
        N = len(dominoes)
        res = len(dominoes) * [0]
        for idx, d in enumerate(dominoes):
            # check right topple force
            if d == 'R':
                f = N
            elif d == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            res[idx] += f
        
        for idx, d in enumerate(dominoes[::-1], 1):
            # check left topple force
            if d == 'L':
                f = N
            elif d == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            res[-idx] -= f
        
        temp = []
        for f in res:
            if f < 0:
                temp.append('L')
            elif f > 0:
                temp.append('R')
            else:
                temp.append('.')
        return ''.join(temp)
        
