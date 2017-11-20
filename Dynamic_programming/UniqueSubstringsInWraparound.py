# LeetCode 467. Unique Substrings in Wraparound String
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        counts = [0] * 26
        cur_max = 0
        for i, char in enumerate(p):
            if i == 0:
                cur_max = 1
            elif ord(char) % 26 == (ord(p[i-1]) + 1) % 26:
                cur_max += 1
            else:
                cur_max = 1
            index = ord(char)-97
            counts[index] = max(counts[index], cur_max)
        return sum([count for count in counts])
