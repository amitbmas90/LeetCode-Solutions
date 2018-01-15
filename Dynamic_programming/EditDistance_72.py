# O(mn) run-time, space complexity O(mn).
# Tricky point: when substring lengths are same, replace is not always optimal. Counter example: "sea" and "eat".
# 1146 / 1146 passed, beat 95%.
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        
        def dp(i, j):
            # find solution for substring word1[:i+1] and word2[:j+1]
            if (i, j) not in memo:
                res = None
                if i < 0 or j < 0: 
                    res = max(i+1, j+1)
                elif word1[i] == word2[j]:
                    res = dp(i-1, j-1)
                else:
                    res = min(dp(i-1, j-1), dp(i-1, j), dp(i, j-1)) + 1
                memo[i, j] = res
            return memo[i, j]
        
        m, n = len(word1), len(word2)
        dp(m-1, n-1)
        return memo[m-1, n-1]
