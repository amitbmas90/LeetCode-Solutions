import collections


class Solution:
    def checkInclusion(self, s1, s2):
        """
        Sliding window solution
        O(len(s2)) time-complexity
        O(len(s1)) extra-space

        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        k = len(s1)
        missing = k
        need = collections.Counter(s1)

        for ix, c in enumerate(s2):
            missing -= need[c] > 0
            if c in need:
                need[c] -= 1

            if ix >= k:
                prev = s2[ix - k]
                # if previous character is not in s1, it does not affect missing count
                if prev in need:
                    need[prev] += 1
                    # if after pop the earlier character we are missing some character in s1,
                    # add 1 to missing
                    if need[prev] > 0:
                        missing += 1

            if missing == 0:
                return True

        return False
