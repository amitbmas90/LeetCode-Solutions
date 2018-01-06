class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        from re import compile
        t = compile('\*+')
        p = t.sub("*", p)
        dp = {}
        def match(i, j):
            if (i, j) not in dp:
                res = None
                if i == len(s): res = p[j:] == "" or p[j:] == "*"
                elif j == len(p): res = i == len(s)
                elif p[j] == "*":
                    res = match(i+1, j) or match(i, j+1)
                elif p[j] in {s[i], "?"}:
                    res = match(i+1, j+1)
                else:
                    res = False
                dp[i, j] = res
            return dp[i, j]
        
        return match(0, 0)
