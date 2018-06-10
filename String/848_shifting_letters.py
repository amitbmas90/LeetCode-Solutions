# O(N) run-time and O(N) space-complexity
from string import ascii_lowercase as alphabet
class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        A = alphabet
        s = []      # accumulated shifts
        count = 0
        for shift in shifts[::-1]:
            count += shift
            s.append(count % 26)
        s = s[::-1]
        res = list(S)
        for idx, shift in enumerate(s):
            letter = res[idx]
            index_in_A = ord(letter) - 97
            res[idx] = A[(index_in_A + shift) % 26]
        return ''.join(res)
