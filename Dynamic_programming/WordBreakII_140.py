class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s == None or len(s) == 0: return []
        memo = {len(s): [""]}
        wordDict = set(wordDict)

        def dp(start):
            if start not in memo:
                res = []
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        temp = dp(end)
                        for k in temp:
                            res.append((s[start:end] + " " + k).strip())
                memo[start] = res
            return memo[start]

        dp(0)
        return memo[0]
