class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dp(s):
            if s not in memo:
                for ix, c in enumerate(s):
                    if ix > 0 and c == s[ix - 1] == '+':
                        if not dp(s[:ix - 1] + '--' + s[ix + 1:]):
                            res = True
                            break
                else:
                    res = False
                memo[s] = res
            return memo[s]

        memo = {}
        return dp(s)
