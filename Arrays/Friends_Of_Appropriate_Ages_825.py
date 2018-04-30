class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        counts = [0] * 121
        for age in ages:
            counts[age] += 1
        res = 0
        for a_1, count_1 in enumerate(counts):
            for a_2, count_2 in enumerate(counts[:a_1+1]):
                if a_2 <= 0.5 * a_1 + 7: continue
                if a_2 == a_1: res -= count_1
                res += count_1 * count_2
        return res
        
