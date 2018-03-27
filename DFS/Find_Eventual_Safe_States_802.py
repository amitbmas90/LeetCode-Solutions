# check if a node is part of a cycle.
# maintain previous check results to exit recursion quickly.
# O(V+E) run-time and O(V) space complexity.
class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        colors = [0] * len(graph)
        white, grey, black = 0, 1, 2
        
        def dfs(node):
            if colors[node] != white:
                return colors[node] == black
            colors[node] = grey
            for v in graph[node]:
                if colors[v] == black:
                    continue
                if colors[v] == grey or not dfs(v):
                    return False
            colors[node] = black
            return True
        
        return [v for v in range(len(graph)) if dfs(v)]
