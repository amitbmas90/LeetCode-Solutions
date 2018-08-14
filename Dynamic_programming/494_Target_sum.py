class Solution:
    def findTargetSumWays(self, nums, S):
        """
        Top-down DP. Subproblem is defined as number of ways to reach target T with K numbers.
        The tricky point is when current number is 0. Need special treatment.
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def dp(k, t):
            if (k, t) not in memo:
                if k == 0:
                    res = sum([t == num for num in (nums[0], -nums[0])])
                else:
                    if nums[k] > 0:
                        res = dp(k-1, t-nums[k]) + dp(k-1, t+nums[k])
                    else:
                        res = 2 * dp(k-1, t)
                memo[k, t] = res
            return memo[k, t]

        memo = {}
        dp(len(nums)-1, S)
        return memo[len(nums)-1, S]
