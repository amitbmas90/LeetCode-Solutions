# Python3 solution.
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = list(map(int, str(num)))
        last = {d: i for i, d in enumerate(n)}
        for i, k in enumerate(n):
            for digit in range(9, k, -1):
                if last.get(digit, 0) > i:
                    n[last[digit]], n[i] = n[i], n[last[digit]]
                    return int(''.join(map(str, n)))
        return num
