class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0 : return '0'
        if n == 1: return '1'
        res = ['1']
        for _ in range(1, n):
            count = 0
            newRes = []
            for i, num in enumerate(res):
                if count == 0 or res[i] == res[i-1]:
                    count += 1
                else:
                    newRes.append(str(count))
                    newRes.append(res[i-1])
                    count = 1
            if count > 0:
                newRes.append(str(count))
                newRes.append(res[-1])
            res = newRes
        return ''.join(res)
