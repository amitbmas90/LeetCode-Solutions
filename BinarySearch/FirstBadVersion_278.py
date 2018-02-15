# Second binary search version is applied.
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = l + (r-l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
        if l <= n and isBadVersion(l):
            return l
        return -1
