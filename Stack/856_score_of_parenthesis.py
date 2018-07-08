class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def dfs(i, j):
            stack = 0
            prev = i
            res = 0
            for k in range(i, j):
                if S[k] == '(':
                    stack += 1
                else:
                    stack -= 1
                if stack == 0:
                    if k - prev == 1:
                        res += 1
                    else:
                        res += 2 * dfs(prev+1, k)
                    prev = k+1
            return res
        return dfs(0, len(S))
