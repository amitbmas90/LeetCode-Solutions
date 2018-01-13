# Inspired by JAVA solution of @shawngao
# Find number of palindromic substrings in a string.
# O(N^2) run-time and O(1) space-complexity.
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0: return 0
        self.count = 0
        def Count(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    self.count += 1
                    l -= 1
                    r += 1
                else:
                    break
        for i in range(len(s)):
            Count(i, i)
            Count(i, i+1)
        return self.count
