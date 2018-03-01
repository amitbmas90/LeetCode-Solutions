# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(m, n):
            return m if n == 0 else gcd(n, m % n)
        
        def slope(p1, p2):
            dx = p1.x - p2.x
            dy = p1.y - p2.y
            if dx == 0: return (0, p1.x)
            if dy == 0: return (p1.y, 0)
            k = gcd(dx, dy)
            return dx // k, dy // k
                  
        n = len(points)
        counter = collections.Counter()
        res = 0
        for i in range(n):
            counter.clear()
            samePoints = 1
            maxPoints = 0
            for j in range(i+1, n):
                if points[j].x == points[i].x and points[j].y == points[i].y: samePoints += 1
                else:
                    dx, dy = slope(points[i], points[j])
                    counter[dx, dy] += 1
                    maxPoints = max(maxPoints, counter[dx, dy])
            res = max(res, maxPoints + samePoints)
        return res
