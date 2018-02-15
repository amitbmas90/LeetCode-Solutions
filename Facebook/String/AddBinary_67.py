# Iterative solution. Easily extend to Oct/Hex additions.
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        res, carry = [], 0
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0: 
                _sum += int(a[i])
                i -= 1
            if j >= 0: 
                _sum += int(b[j])
                j -= 1
            carry = _sum // 2
            res.append(str(_sum % 2))
        if carry > 0: res.append(str(carry))        
        return ''.join(res)[::-1]
