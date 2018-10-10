from collections import Counter


class Solution:
    def four_sum_count(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1 = Counter()
        d2 = Counter()

        for a in A:
            for b in B:
                d1[a + b] += 1

        for c in C:
            for d in D:
                d2[c + d] += 1

        res = Counter()
        for k in d1:
            if -k in d2:
                res[k] = d1[k] * d2[-k]

        return sum([val for val in res.values()])
