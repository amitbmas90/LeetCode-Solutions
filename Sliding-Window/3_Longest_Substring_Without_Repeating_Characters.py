class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        res = 0
        left = 0
        for right, c in enumerate(s):
            if c in char_set:
                while s[left] != c:
                    char_set.remove(s[left])
                    left += 1
                left += 1
            else:
                char_set.add(c)
                res = max(res, len(char_set))
        return res
