  # Breadth-first Search
  * Covers topics related to breadth-first search.
  * Include solutions to problems using Kahn's algorithm for **Topological Sort**.
  * In BFS, one important detail is there is a difference between nodes **Visited** and **Visiting**. 
    * For both types of nodes, if seen again from other nodes, should not enqueue again. 
    * This is especially true for finding shortest path in undirected graphs using BFS. 
    The distance from new node to some node cannot be shorter than when the node is first seen.
    * A question arises when considering how to check state of a node in a simplified implementation. 
    One choice is use hash map for tracking and updating status of nodse. Sometimes there is no need to differentiate visiting
    and visited nodes, then a set is enough for this purpose.
  * Cycle detection
    * In directed graph, if any two nodes contains each other as neighbor, there exists a cycle. Topological sort is not possible.
    * In undirected graph, it is often easier to use DFS to detect cycle. 
