# Legal two-digit postfix: 0 <= int(postfix) <= 26
# Legal 1-digit postfix: 0 < int(postfix) <= 9
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        prev, cur = 1, 0
        if int(s[0]) > 0:
            cur = 1 
        for i in range(1, len(s)):
            temp = 0
            if int(s[i]) > 0:
                temp += cur
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += prev
            prev = cur
            cur = temp
        return cur

    
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
