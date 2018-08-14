import collections


class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        color = [0] * (N + 1)  # -1 means red, 1 blue, 0 no color

        first_node = None
        for x, y in dislikes:
            if first_node is None:
                first_node = x
            graph[x].append(y)
            graph[y].append(x)

        if len(graph) == 0:
            return True

        color[first_node] = 1
        q = collections.deque([first_node])

        while q:
            cur = q.popleft()
            cur_color = color[cur]
            for nei in graph[cur]:
                if color[nei] == cur_color:
                    return False
                elif color[nei] == -cur_color:  # visited
                    continue
                color[nei] = -cur_color
                q.append(nei)
        return True
