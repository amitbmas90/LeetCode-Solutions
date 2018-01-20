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

    
    # Top-down approach
    class Solution(object):
        def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            if len(s) == 0: return 0
            memo = {len(s): 1}
            def dp(i):
                if i not in memo:
                    res = 0
                    if s[i] == '0': res = 0
                    elif i == len(s) - 1: res = 1
                    else:
                        res += dp(i+1)
                        if 10 <= int(s[i:i+2]) < 27:
                            res += dp(i+2)
                    memo[i] = res
                return memo[i]

            dp(0)
            return memo[0]
