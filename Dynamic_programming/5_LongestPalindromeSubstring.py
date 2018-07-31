class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) == 0: return 0
        I = J = 0
        
        def expand(l, r):
            nonlocal I, J
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > J - I:
                    I, J = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return s[I:J+1]
