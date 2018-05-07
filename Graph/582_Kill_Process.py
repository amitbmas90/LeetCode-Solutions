# O(N) run-time and O(N) space complexity. 
# We need to traverse over the pid array once.
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        res = []
        graph = collections.defaultdict(list)   # stores directed-graph neighbors
        for parent, child in zip(ppid, pid):
            graph[parent].append(child)
        def dfs(node):
            res.append(node)
            for child in graph[node]:
                dfs(child)
        dfs(kill)
        return res
        
