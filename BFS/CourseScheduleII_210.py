# Topological sort via BFS with O(E) run-time. |E| is no smaller than |N| since the graph is connected.
# Space-complexity O(E). 44/44, 87ms, Beat 70%.
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses
        for x, y in prerequisites:
            indegrees[x] += 1
            graph[y].append(x)
            
        queue = collections.deque()
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(node)
                
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for neighbor in graph[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []
