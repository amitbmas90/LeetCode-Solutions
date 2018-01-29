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
            left_min = [sys.maxsize] * K
            right_min = [sys.maxsize] * K
            for j, cost in enumerate(prev):
                left_min[j] = min(cost, left_min[j-1]) if j > 0 else cost   
            for j in range(K-1, -1, -1):
                right_min[j] = min(prev[j], right_min[j+1]) if j < K - 1 else prev[j]                 
            for j, cost in enumerate(costs[i]):
                if j > 0 and j < K - 1:
                    cur[j] = cost + min(left_min[j-1], right_min[j+1])
                elif j == 0:
                    cur[j] = cost + right_min[1]
                else:
                    cur[j] = cost + left_min[K-2]
            prev = cur
        
        return min(prev)
