class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        for i in range(min(N, 10)):
            x = int(S[:i + 1])
            if x != 0 and S[:i + 1].startswith('0'):
                break
            for j in range(i + 1, min(N, i + 10)):
                y = int(S[i + 1: j + 1])
                if y != 0 and S[i + 1: j + 1].startswith('0'):
                    break
                fib = [x, y]
                cur = j + 1
                while cur < N:
                    a, b = fib[-2], fib[-1]
                    z = str(a + b)
                    if a + b <= 2 ** 31 - 1 and S[cur:].startswith(z):
                        fib.append(a + b)
                        cur += len(z)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []
