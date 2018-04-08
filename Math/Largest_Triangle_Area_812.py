class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(a, b, c):
            return abs(a[0]*(b[1]-c[1])+ b[0]*(c[1]-a[1])+ c[0]*(a[1]-b[1])) / 2.0
        res = 0.0
        for x, p_x in enumerate(points[:-2]):
            for y, p_y in enumerate(points[x+1:-1]):
                for z, p_z in enumerate(points[y+1:]):
                    res = max(res, area(p_x, p_y, p_z))
        return res
            
