# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None
        m = {}
        queue = collections.deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur not in m:
                m[cur] = UndirectedGraphNode(cur.label)
            for neighbor in cur.neighbors:
                if neighbor not in m:
                    m[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                m[cur].neighbors.append(m[neighbor])            
        return m[node]
