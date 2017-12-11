# Given a m * n map with no islands, and a sequence of positions to build islands at particular positions. 
# Count the number of islands along with the building operations.
# Union-find with ranking. Challenges: how to index groups and how to merge islands.
# Time complexity O(Klog(mn)), K is the number of positions.
class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find(x, y):
            gx, gy = groups[x][y]
            if (gx, gy) == (x, y):
                return x, y
            return find(gx, gy)
        
        def union(*args):
            x1, y1, x2, y2 = args
            gx1, gy1 = find(x1, y1)
            gx2, gy2 = find(x2, y2)
            if (gx1, gy1) == (gx2, gy2): 
                return 0                                # in the same group
            if rank[x1][y1] > rank[x2][y2]:
                groups[gx2][gy2] = groups[gx1][gy1]
            elif rank[x1][y1] < rank[x2][y2]:
                groups[gx1][gy1] = groups[gx2][gy2]
            else:
                groups[gx1][gy1] = groups[gx2][gy2]
                rank[gx2][gy2] += 1
            return 1
            
        numIslands = 0
        res = []
        maps = [[0]* n for _ in range(m)]
        groups = [[(i, j) for j in range(n)] for i in range(m)]
        rank = [[0]* n for _ in range(m)]
        for position in positions:
            x, y = position
            maps[x][y] = 1
            numIslands+=1
            for dx, dy in zip([-1, 1, 0, 0],[0, 0, 1, -1]):
                x1, y1 = x+dx, y+dy
                if 0 <= x1 < m and 0 <= y1 < n and maps[x1][y1]==1:
                    numIslands-=union(x,y, x1,y1)
            res.append(numIslands)
        return res        
