class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # default level 1 operator as plus, level 2 operator as multiplication
        op1, op2 = 1, 1
        # default level 1, level 2 results
        p1, p2 = 0, 1

        ix = 0
        while ix < len(s):
            c = s[ix]
            if c.isdigit():
                val = int(c)
                while ix + 1 < len(s) and s[ix + 1].isdigit():
                    val = 10 * val + int(s[ix + 1])
                    ix += 1
                if op2 == 1:
                    p2 *= val
                else:
                    p2 //= val
            elif c == '+' or c == '-':
                p1 = p1 + op1 * p2
                p2, op2 = 1, 1
                op1 = 1 if c == '+' else -1
            elif c == '*' or c == '/':
                op2 = 1 if c == '*' else 0
            ix += 1
        return p1 + op1 * p2
