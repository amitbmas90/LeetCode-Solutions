# Solution without extra space, and without reverse. Key is multiply from high digits to lower digits
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        cur = 0
        for a in num1:
            cur *= 10
            temp = 0
            for b in num2:
                temp *= 10
                temp += int(a) * int(b)
            cur += temp
        return str(cur)


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
