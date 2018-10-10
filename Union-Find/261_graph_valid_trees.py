# Given a graph of n nodes, expressed as a list of edges. Find if these edges form a tree.
# Union-find-rank. beat 86% Python.
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        ranks = [0] * n
        groups = list(range(n))
        def find(x):
            if groups[x] == x:
                return x
            return find(groups[x])
        
        def union(x, y):
            gx, gy = find(x), find(y)
            if gx == gy: return False
            if ranks[gx] < ranks[gy]:
                groups[gx] = gy
            elif ranks[gx] > ranks[gy]:
                groups[gy] = gx
            else:
                ranks[gx] += 1
                groups[gy] = gx
            return True
        
        for x, y in edges:
            if not union(x, y): return False

        one_group = find(0)
        for k in range(1, n):
            if find(k) != one_group:
                return False
        return True
