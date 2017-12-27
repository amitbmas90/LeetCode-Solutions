# DFS to check cycle and visit at the same time. Union-find solution is at /Union-find folder.
# stats: 69ms, beat 79%
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        visited = {v: False for v in range(n)}
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        def dfs(v, parent, graph):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, v, graph):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        if dfs(0, None, graph): return False
        return all([visited[v] for v in visited])
