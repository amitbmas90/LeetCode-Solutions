class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        up = down = res = 0
        for idx, num in enumerate(A[1:], 1):
            if down and num > A[idx-1] or num == A[idx-1]:
                up = down = 0   # reset when seeing up-slope or flat
            up += num > A[idx-1]
            down += num < A[idx-1]
            if up and down:
                res = max(res, up+down+1)
        return res
    