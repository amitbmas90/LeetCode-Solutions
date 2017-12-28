# Legal two-digit postfix: 0 <= int(postfix) <= 26
# Legal 1-digit postfix: 0 < int(postfix) <= 9
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==None or len(s)==0: return 0
        memo = [0] * (len(s) + 1)
        memo[0] = 1
        if s[0] != '0':
            memo[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] != '0': 
                memo[i] += memo[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                memo[i] += memo[i-2]
        return memo[len(s)]
