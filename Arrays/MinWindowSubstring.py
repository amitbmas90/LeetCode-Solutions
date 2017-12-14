# Solution by StefanPochman
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # after creating a complete window, the invariance is maintained
        counter, missing = collections.Counter(t), len(t)
        i, rs, rt = 0, 0, 0
        for j, c in enumerate(s, 1):
            missing -= counter[c] > 0
            counter[c] -= 1
            if not missing:
                while i < j and counter[s[i]] < 0:
                    counter[s[i]] += 1
                    i += 1
                if not rt or j - i <= rt - rs:
                    rt, rs = j, i
        return s[rs:rt]
