class Solution:
    def generateParenthesis(self, n):
        """
        a valid parentheses string has to be # left parenthesis >= # right parenthesis
        :type n: int
        :rtype: List[str]
        """
        def dfs(path, left_count, right_count, res):
            """
            traverse from one string to another
            stop if the path is invalid
            """
            if left_count == right_count == n:
                res.append(''.join(path))
            elif left_count > n or right_count > n or left_count < right_count:
                return
            elif left_count == right_count:
                dfs(path + ['('], left_count + 1, right_count, res)
            else:
                dfs(path + ['('], left_count + 1, right_count, res)
                dfs(path + [')'], left_count, right_count + 1, res)

        res = []
        dfs([], 0, 0, res)
        return res
