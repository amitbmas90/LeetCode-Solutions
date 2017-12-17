class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def DFS(res, path, myDict, depth):
            if depth==len(digits):
                res.append(''.join(path))
            else:
                for i in range(len(myDict[digits[depth]])):
                    DFS(res, path + [myDict[digits[depth]][i]], myDict, depth+1)

        myDict = {'0':[' '], '1':['*'], '2': list('abc'), '3': list('def'), '4': ('ghi'),
        '5': list('jkl'), '6': list('mno'), '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}

        res = []
        path = []

        DFS(res, path, myDict, 0)
        return res if len(digits) > 0 else []

digits = "2312"
print( letterCombinations(digits))
