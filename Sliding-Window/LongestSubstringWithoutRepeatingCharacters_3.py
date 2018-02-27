class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        if s == None or len(s) == 0:
            return 0
        cnt = collections.Counter()
        l = r = 0
        res = 0
        while r < len(s):
            count = cnt[s[r]]
            if count == 0:
                cnt[s[r]] = 1
            else:
                while l < r and s[l] != s[r]:
                    cnt[s[l]] -= 1
                    l += 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
