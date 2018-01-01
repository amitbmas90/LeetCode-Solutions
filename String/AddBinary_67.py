class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1, l2 = len(a)-1, len(b)-1
        res = []
        carry = 0
        while l1 >= 0 or l2 >= 0:
            temp = carry
            if l1 >= 0: 
                temp += ord(a[l1]) - ord('0')
                l1 -= 1
            if l2 >= 0:
                temp += ord(b[l2]) - ord('0')
                l2 -= 1
            carry = temp // 2
            res.append(chr(temp % 2 + ord('0')))
        if carry != 0:
            res.append(chr(carry + ord('0')))
        return ''.join(reversed(res))
                
