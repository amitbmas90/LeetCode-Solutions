# Implement a simplified A* Search algorithm for the tree cutting problem. TLE...
from heapq import heappush, heappop
class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # Since we can only move in 4 directions, use Manhattan distance as heuristic.
        
        def astar(sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            q = [(0, 0, sr, sc)]
            visiting = {(sr, sc): True}
            visited = set()
            gcosts = {(sr, sc): 0}
            while q:
                f, g, r, c = heappop(q)
                visited.add((r,c))
                visiting[(sr,sc)] = False
                if r == tr and c == tc:
                    return g
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (0 <= nr < R and 0 <= nc < C and forest[nr][nc]) and (nr, nc) not in visited:
                        if (nr,nc) not in visiting or visiting[(nr,nc)] == False:
                            visiting[(nr, nc)] = True
                            newg = g + 1
                            if newg < gcosts.get((nr,nc), 999):
                                gcosts[(nr, nc)] = newg
                                fcost = newg + abs(nr - tr) + abs(nc - tc)
                                heappush(q, (fcost, newg, nr, nc))
            return -1
                
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr, sc, res = 0, 0, 0
        for tree in trees:
            v, tr, tc = tree
            d = astar(sr, sc, tr, tc)
            if d < 0: return -1
            res += d
            sr, sc = tr, tc
        return res
