# Union-find by rank. 
# Run time O(N*α(P) + P*α(P)), where P is number of pairs and alpha(P) is the time for checking if two strings are in the same group. 
# P * α(P)) is the union time. α is the Inverse-Ackermann function.
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        cnt, d = 0, {}
        for pair in pairs:
            x, y = pair
            if x not in d:
                d[x] = cnt
                cnt += 1
            if y not in d:
                d[y] = cnt
                cnt += 1
        groups = [-1] * len(d)
        ranks = [0] * len(d)
        def find(x):
            if groups[x] == -1:
                return x
            return find(groups[x])

        def union(x, y):
            g_x = find(x)
            g_y = find(y)
            if g_x == g_y: return
            if ranks[g_x] > ranks[g_y]:
                groups[g_y] = g_x
            elif ranks[g_x] < ranks[g_y]:
                groups[g_x] = g_y
            else:
                groups[g_x] = g_y
                ranks[g_y] += 1

        for pair in pairs:
            x, y = pair
            n_x, n_y = d[x], d[y]
            union(n_x, n_y)

        for x, y in zip(words1, words2):
            if x == y: continue
            if x not in d or y not in d: return False
            gx = find(d[x])
            gy = find(d[y])
            if gx != gy:
                return False
        return True
