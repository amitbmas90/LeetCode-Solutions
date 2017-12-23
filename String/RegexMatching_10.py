# the most tricky part is how to deal with '*'
# Need to look forward for matching the star.
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        d = {}
        def dp(i, j):
            if (i, j) not in d:
                res = None
                if j == len(p):
                    res = i == len(s)
                else:
                    match_first = i < len(s) and p[j] in {s[i], '.'}
                    if j < len(p) - 1 and p[j+1] == '*':
                        # tricky part: skip current character 
                        # or second case, continue use pattern of 'k*'
                        res = dp(i, j+2) or match_first and dp(i+1, j)
                    else:
                        res = match_first and dp(i+1, j+1)
                d[i, j] = res
            return d[i, j]
        dp(0,0)
        return d[0, 0]
