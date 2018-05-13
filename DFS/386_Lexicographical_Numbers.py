# O(n) run-time, O(1) space-complexity.
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def dfs(cur_sum):
            if cur_sum > n:
                return
            res.append(cur_sum)
            cur_sum *= 10
            for i in range(10):
                dfs(cur_sum + i)
        for i in range(1, min(10, n+1)):
            dfs(i)
        return res
    
