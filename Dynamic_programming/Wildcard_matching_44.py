class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def match(i, j):
            if (i, j) not in memo:
                res = True
                if i == len(s):
                    if j < len(p):
                        if p.count('*', j) != len(p) - j: res = False
                elif j == len(p): res = i == len(s)
                else:
                    if p[j] in {s[i], '?'}: res = match(i+1, j+1)
                    elif p[j] == '*': res = match(i, j+1) or match(i+1, j)
                    else: res = False
                memo[i, j] = res
            return memo[i, j]
        return match(0, 0)
