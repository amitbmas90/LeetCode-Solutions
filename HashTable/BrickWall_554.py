# O(N) run-time, N is number of bricks
# Worst-case scenario for previously failed array-based counting: bricks are almost as big as each row width.
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall == None or len(wall) == 0: return 0
        total_width = sum(wall[0])
        count = {}
        for row in wall:
            _sum = 0
            for brick in row[:-1]:
                _sum += brick
                count[_sum] = count.get(_sum, 0) + 1
        res = sys.maxsize
        for k in count:
            res = min(res, len(wall) - count[k])
        return res if res < sys.maxsize else len(wall)
