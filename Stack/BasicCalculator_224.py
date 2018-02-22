class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        i = 0
        sign = 1
        while i < len(s):
            if s[i].isdigit():
                val = int(s[i])
                while i + 1 < len(s) and s[i+1].isdigit():
                    val = val * 10 + int(s[i+1])
                    i += 1
                res += sign * val
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif s[i] == ')':
                res = stack.pop() * res + stack.pop()
            i += 1
        return res
