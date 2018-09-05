class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def dfs(x, y, visited):
            """
            search for result of x / y
            if not found, return -1.0
            """
            visited.add(x)
            if (x, y) not in known:
                for nei in graph[x]:
                    if nei not in visited:
                        res = dfs(nei, y, visited)
                        if res != -1.0:
                            known[x, y] = known[x, nei] * res
                            known[y, x] = 1 / known[x, y]
                            break
                else:
                    known[x, y] = -1.0
            visited.remove(x)
            return known[x, y]

        known = {}
        graph = collections.defaultdict(set)
        for equation, val in zip(equations, values):
            x, y = equation
            graph[x].add(x)
            graph[x].add(y)
            graph[y].add(x)
            graph[y].add(y)
            known[x, y] = val
            known[y, x] = 1 / val
            known[x, x] = 1.0
            known[y, y] = 1.0

        res = []
        for x, y in queries:
            if x not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(x, y, set()))

        return res
