# BFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return node
        q = collections.deque()
        q.append(node)
        d = {}
        d[node] = UndirectedGraphNode(node.label)
        while q:
            n = q.popleft()
            for k in n.neighbors:
                if k not in d:
                    neighbor = UndirectedGraphNode(k.label)
                    d[n].neighbors.append(neighbor)
                    d[k] = neighbor
                    q.append(k)
                else:
                    d[n].neighbors.append(d[k])
        return d[node]
        
 # DFS
 class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.cloneMap = {}
        
    def cloneGraph(self, node):
        if node == None: return None
        if node in self.cloneMap: return self.cloneMap[node]
        self.cloneMap[node] = UndirectedGraphNode(node.label)
        for n in node.neighbors:
            self.cloneMap[node].neighbors.append(self.cloneGraph(n))
        return self.cloneMap[node]
