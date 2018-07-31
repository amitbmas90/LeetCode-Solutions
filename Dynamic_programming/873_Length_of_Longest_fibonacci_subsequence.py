import collections


class Solution:
    """
    The sub-problem is quite subtle.
    Let opt[i, j] be the length of longest fibonacci sub-sequence ending at i, j.
    Also the minimal length equals 2.
    """
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        opt = collections.defaultdict(lambda: 2)
        indexes = {x: i for i, x in enumerate(A)}
        res = 0
        for i, n in enumerate(A):
            for k in range(i):
                ix = indexes.get(n - A[k], None)
                if ix is not None and ix < k:
                    opt[A[k], n] = opt[n - A[k], A[k]] + 1
                    res = max(res, opt[A[k], n])
        return res if res >= 3 else 0
