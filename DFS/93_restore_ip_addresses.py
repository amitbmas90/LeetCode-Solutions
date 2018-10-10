class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(path, r_s, res):
            """
            path: list[str]

            r_s: str
                remaining string

            res: list[str]
                result

            return: void
            """
            if len(path) == 4 and len(r_s) == 0:
                res.append('.'.join(path))
            elif len(r_s) == 0 or len(r_s) > 0 and len(path) == 4:
                return
            else:
                if len(r_s) > 0:
                    dfs(path + [r_s[:1]], r_s[1:], res)
                if len(r_s) > 1 and r_s[0] != '0':
                    dfs(path + [r_s[:2]], r_s[2:], res)
                if len(r_s) > 2 and r_s[0] != '0' and int(r_s[:3]) < 256:
                    dfs(path + [r_s[:3]], r_s[3:], res)

        res = []
        dfs([], s, res)
        return res
