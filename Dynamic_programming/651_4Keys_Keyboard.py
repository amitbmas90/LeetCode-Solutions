class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N+1)
        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1
            for j in range(1, i-2):
                # we can copy at most from i - 3 location and
                # the optimal value for that location is dp[j]
                times_copied = i - (j + 3) + 1
                dp[i] = max(dp[i], dp[j] + times_copied * dp[j])
        return dp[N]
