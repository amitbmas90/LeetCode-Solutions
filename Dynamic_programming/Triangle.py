# LeetCode Problem 120.
# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        prev = None
        for i in range(rows-1, -1, -1):
            cur = triangle[i]
            if i < rows - 1:
                for j in range(len(cur)):
                    cur[j] += min(prev[j], prev[j+1])
            prev = cur
        return prev[0]
