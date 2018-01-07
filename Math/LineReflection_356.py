# O(N) time complexity, O(N) space complexity
class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points == None or len(points) < 2: return True  
        min_x = float('inf')
        max_x = -float('inf')
        s = set()
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            s.add(str(x) + ' ' + str(y))      
        sum_ = max_x + min_x
        for point in s:
            x, y = point.split(" ")
            new_x = sum_ - int(x)
            if str(new_x)+" "+str(y) not in s: return False
        return True
