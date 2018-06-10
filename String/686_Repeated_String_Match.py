class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        x = math.ceil(n / m)
        if B in A*x:
            return x
        elif B in A*(x+1):
            return x+1
        return -1
    