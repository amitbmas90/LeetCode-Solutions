class Solution:
    def is_bipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(node, color):
            res = True
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = -color[node]
                    if not dfs(nei, color):
                        res = False
                elif color[nei] == color[node]:
                    return False
            return res

        color = {}
        n_nodes = len(graph)
        for node in range(n_nodes):
            if node not in color:
                color[node] = 1
                if not dfs(node, color):
                    return False
        return True
