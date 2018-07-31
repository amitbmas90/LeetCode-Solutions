import collections


class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        q_a = collections.deque(sorted(A))
        q_b = collections.deque(sorted(B))
        d = collections.defaultdict(list)
        unused = []
        while q_a:
            cur = q_a.popleft()
            if cur > q_b[0]:
                d[q_b.popleft()].append(cur)
            else:
                unused.append(cur)
        res = []
        for val in B:
            if val in d and len(d[val]) > 0:
                res.append(d[val].pop())
            else:
                res.append(unused.pop())
        return res
