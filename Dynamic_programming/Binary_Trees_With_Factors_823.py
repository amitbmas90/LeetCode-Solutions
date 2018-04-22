class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = 10**9 + 7
        A.sort()
        res = 0
        dp = {num:1 for num in A}
        for i, a in enumerate(A):
            for b in A[:i]:
                if a % b == 0:
                    right = a // b
                    if right in dp:
                        dp[a] += dp[b] * dp[right]
        res = sum([dp[num] for num in dp]) % N
        return res
        
