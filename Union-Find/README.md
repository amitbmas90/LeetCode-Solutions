# Union-Find Data Structure
  ## In an undirected graph, Union-find DS is used to find connected components in the graph.
  * First step to apply union-find is to define nodes and edges. 
  * Initialize the group of each node by its key or index. Initialize the rank of each node with 0.
  * Find function finds the ancestor of a group and union function unites two groups if we found some edge connecting 
  nodes in each group.
  * Standard Python Union-by-Rank data structure:
  ```
  class Union-Find:
      def find(x):
          if groups[x] == x:  return x
          return find(groups[x])

      def union(x, y):
          group_x = find(x)
          group_y = find(y)
          if group_x != group_y:
              if rank[x] > rank[y]:
                  groups[group_y] = groups[group_x]
              elif rank[x] < rank[y]:
                  groups[group_x] = groups[group_y]
              else:
                  rank[group_x] += 1
                  groups[group_y] = group_x
  ```
