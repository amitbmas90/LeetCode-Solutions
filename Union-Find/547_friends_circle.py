class UF:
    def __init__(self, n):
        self.groups = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.groups[x] == x:
            return x
        return self.find(self.groups[x])

    def union(self, x, y):
        gx = self.find(x)
        gy = self.find(y)
        if gx == gy: return
        if self.ranks[gx] > self.ranks[gy]:
            self.groups[gy] = gx
        elif self.ranks[gx] < self.ranks[gy]:
            self.groups[gx] = gy
        else:
            self.ranks[gx] += 1
            self.groups[gy] = gx


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def num_groups(uf):
            s = set()
            for g in range(len(uf.groups)):
                s.add(uf.find(g))
            return len(s)

        N = len(M)  # we know it is N * N
        uf = UF(N)
        for i in range(N):
            for j in range(i):
                if M[i][j] == 1:
                    uf.union(i, j)

        return num_groups(uf)
