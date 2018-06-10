import collections
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        N = len(quiet)
        res = [None] * N
        graph = [[] for _ in range(N)]
        indegrees = [0] * N
        for x, y in richer:
            graph[y].append(x)
            indegrees[x] += 1

        def dfs(node):
            if res[node] is None:
                res[node] = node
                for child in graph[node]:
                    candidate = dfs(child)
                    if quiet[candidate] < quiet[res[node]]:
                        res[node] = candidate
            return res[node]

        for node in range(N):
            if indegrees[node] == 0:
                dfs(node)

        return res

# richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
# quiet = [3,2,5,4,6,1,7,0]
