# 一定要想清楚边界，dp[i] means breakable of substring of [0,i). So for subproblem dp[j] the range is also to [0,i) 
# Bottom-up approach
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]



# Top-down approach
class Solution_top_down:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        memo = {len(s): True}

        def breakable(s, start, memo):
            if start not in memo:
                res = False
                for j in range(start+1, len(s)+1):
                    if breakable(s, j, memo) and s[start:j] in wordDict:
                        res = True
                memo[start] = res
            return memo[start]
        return breakable(s, 0, memo)
