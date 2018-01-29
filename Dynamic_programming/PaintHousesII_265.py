# O(NK) run-time, N is number of houses, K is number of colors.
# Space complexity: O(K)
class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        prev = costs[0]
        cur = None
        K = len(costs[0])
        for i in range(1, len(costs)):
            cur = [0] * K
            left_min = [sys.maxsize] * (K+1)
            right_min = [sys.maxsize] * (K+1)
            for j, cost in enumerate(prev, 1):
                left_min[j] = min(cost, left_min[j-1])
            for j in range(K-1, -1, -1):
                right_min[j] = min(prev[j], right_min[j+1])               
            for j, cost in enumerate(costs[i]):
                cur[j] = cost + min(left_min[j], right_min[j+1])
            prev = cur
        
        return min(prev)
