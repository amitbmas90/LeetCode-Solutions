# Java ref: https://segmentfault.com/a/1190000003797204
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == None or len(num) == 0: return []
        res = []
        def dfs(curSum, prev, start, path):
            if start == len(num):
                if curSum == target:
                    res.append("".join(path))
                    return
            for i in range(start+1,len(num)+1):
                cur = num[start:i]
                val = int(cur)
                if len(cur) > 1 and cur[0] == '0': return
                if start == 0:
                    dfs(val, val, i, path+[cur])
                else:
                    dfs(curSum+val, val, i, path+['+', cur])
                    dfs(curSum-val, -val, i, path+['-', cur])
                    dfs(curSum-prev+prev*val, prev*val, i, path+['*', cur])
        dfs(0, 0, 0, [])
        return res
