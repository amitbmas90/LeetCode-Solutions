# Inspired by beautiful solution from @YAVINCI
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        M = len(num1)
        N = len(num2)
        res = [0] * (M+N)
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                temp = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                p1, p2 = i+j, i+j+1
                temp += res[p2]
                res[p1] += temp // 10
                res[p2] = temp % 10
        ret = 0
        for num in res:
            ret = ret * 10 + num
        return str(ret)
