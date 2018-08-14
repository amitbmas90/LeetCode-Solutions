  # Breadth-first Search (BFS)
  * Covers topics related to breadth-first search.
  * Include solutions to problems using Kahn's algorithm for **Topological Sort** for directed graphs.
  * In BFS, one important detail is there is a difference between nodes **Visited** and **Visiting**. 
    * For both types of nodes, if seen again from other nodes, should not enqueue again. 
    * This is especially true for finding shortest path in unweighted graphs using BFS. 
    The distance from new node to some node cannot be shorter than when the node is first seen. 
    * As for how to check the state of a node in a simplified implementation. 
    One option is use hash map for tracking and updating status of nodes. Sometimes there is no need to differentiate visiting
    and visited nodes, then a set is enough for this purpose.
  * Cycle detection
    * In directed graph, if any two nodes contains each other as neighbor, there exists a cycle. Topological sort is not possible. There exists cycle if topological ordering does Not contain all nodes.
    * In undirected graph, it is often easier to use depth-first search to detect cycle.

  * Python template for using BFS to find a shortest path from source to target. Returns -1 if target cannot be found.
  ```
  def BFS(source, target):
        queue = collections.deque([source])
        visited = set()
        dist = 0

        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node == target:
                    return dist
                visited.add(node)
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
            dist += 1
        return -1
  ```
