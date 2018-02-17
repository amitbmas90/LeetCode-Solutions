class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '': return []
        d = {'0':[],'1':[], '2':list('abc'), '3': list('def'), '4': list('ghi'), '5': list('jkl'), 
            '6': list('mno'), '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}
        def dfs(path, idx):
            if idx == len(digits):
                res.append(''.join(list(path)))
            elif digits[idx] not in {'0', '1'}:
                for k in d[digits[idx]]:
                    dfs(path+[k], idx+1)
        res = []
        dfs([], 0)
        return res
            
