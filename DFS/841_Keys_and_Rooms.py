class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(cur):
            nonlocal visited
            if cur in visited:
                return
            visited.add(cur)
            for room in rooms[cur]:
                dfs(room)
        visited = set()
        dfs(0)
        return len(list(visited)) == len(rooms)
